import pandas as pd
import jieba
import re
import os

def get_paras(text:str):
    text = re.sub(r'第.+章', '', text)
    text = re.sub(r'\b○\b', '零', text)
    text = re.sub(r'\d+', '', text) # Remove all the numbers

    text_no_n = text.rstrip()
    paragraphs = [t.strip() for t in text_no_n.split("\n") if len(t.strip()) > 0]
    filtered_paragraphs = [p for p in paragraphs if not (p.startswith('www') or re.match(r'\[.*?\]', p)) and contains_chinese(p) and len(p)>3]

    return filtered_paragraphs

def contains_chinese(text:str):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def statistics(folder_path:str):
    sta = {'Author':[], 'Works Contained':[], 'Total Para Count':[]}
    files = os.listdir(folder_path)
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.isfile(file_path):
            try:
                f = open(file_path,"r",encoding='utf-8')
                author = file_name.split('_')[0]
                work = [file_name.split('_')[1][:-4]]
                paras = get_paras(f.read())
            except UnicodeDecodeError:
                print(f"UnicodeDecodeError: Failed to decode file '{file_name}'. Skipping...")
                continue

            update_dictionary(sta, author, work, len(paras))
        
    print(sta)
    return pd.DataFrame(sta)

def update_dictionary(sta, author, work, para_count):
    if author in sta['Author']:
        index = sta['Author'].index(author)
        sta['Works Contained'][index].extend(work)
        sta['Total Para Count'][index] += para_count
    else:
        sta['Author'].append(author)
        sta['Works Contained'].append(work)
        sta['Total Para Count'].append(para_count)

if __name__ == '__main__':
    fp = 'data/Foreign'
    df = statistics(fp)
    df.to_excel('output.xlsx')
    

    

