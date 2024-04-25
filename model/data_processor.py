# -*- coding: utf-8 -*-

import pandas as pd
import jieba
import re
import os
from tqdm import tqdm
import json


label2ind = {}

def get_paragraphs(text:str):
    text = re.sub(r'第.+章', '', text)
    text = re.sub(r'\d+', '', text) # Remove all the numbers

    text_no_n = text.rstrip()
    paragraphs = [t.strip() for t in text_no_n.split("\n") if len(t.strip()) > 0]
    filtered_paragraphs = [p for p in paragraphs if not (p.startswith('www') or re.match(r'\[.*?\]', p)) and contains_chinese(p) and len(p)>3]

    return filtered_paragraphs

def contains_chinese(text:str):
    return bool(re.search(r'[\u4e00-\u9fff]', text))

def preprocess(folders_path, out_path = 'data/files/train.txt', label2ind_path = 'data/files/label2ind.json'): # For FastText only
    output = open(out_path, "w", encoding='utf-8') 
    label2ind_json = open(label2ind_path, "w", encoding='utf-8') 

    for folder_path in folders_path:
        files = os.listdir(folder_path)
        for file_name in tqdm(files):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                try:
                    f = open(file_path,"r",encoding='utf-8')
                    author = file_name.split('_')[0]
                    if author not in label2ind.keys():
                        label2ind[author] = "__label__" + str(len(label2ind))
                    paras = get_paragraphs(f.read())
                    paras = clean_paragraph(paras, label2ind[author])

                    output.writelines(paras)
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError: Failed to decode file '{file_name}'. Skipping...")
                    continue

    label2ind_json.write(json.dumps(label2ind, ensure_ascii = False))

def clean_paragraph(paras:list[str], label):
    new_paras = []
    temp = []
    for each in paras:
        each = each.rstrip()
        each = each.replace('\n', '')
        each = re.sub(r'\s+', ' ', each)
        each = re.sub(r'\b○\b', '零', each)
        each = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', each)
        words = jieba.cut(each)
        stopwords = list(open(r'data/files/stopwords.txt','r', encoding='utf-8'))   
        clean_words = [word for word in words if word not in stopwords]
        if(len(clean_words) > 2):
            new_paras.append(label + " "+ " ".join(clean_words) + "\n")
            #temp.extend(clean_words)
            #if(len(temp) > 50):
                #new_paras.append(label + " "+ " ".join(temp) + "\n")
                #temp = [] 

    return new_paras
        

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
                paras = get_paragraphs(f.read())
            except UnicodeDecodeError:
                print(f"UnicodeDecodeError: Failed to decode file '{file_name}'. Skipping...")
                continue

            if author in sta['Author']:
                index = sta['Author'].index(author)
                sta['Works Contained'][index].extend(work)
                sta['Total Para Count'][index] += len(paras)
            else:
                sta['Author'].append(author)
                sta['Works Contained'].append(work)
                sta['Total Para Count'].append(len(paras))
        
    return pd.DataFrame(sta)

def text_predict(text):
    text = text.rstrip()
    text = text.replace('\n', '')
    text = text.replace('·', ' ')
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\b○\b', '零', text)
    text = re.sub(r'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', '', text)
    words = jieba.lcut(text)
    return " ".join(words)

def find_works_contained(author_names:list[str]):
    df = pd.read_excel('data/files/info.xlsx')
    works_dict = {}
    for author_name in author_names:
        works_contained = df.loc[df['Author'] == author_name, 'Works Contained'].tolist()
        works_dict[author_name] = works_contained
    return works_dict

if __name__ == '__main__':
    df = statistics('data/Foreign')
    df.to_excel('data/files/info.xlsx')
    preprocess(['data/燃冬有好兆头', 'data/Foreign'])
