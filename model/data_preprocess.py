# 非常draft的一个版本 很乱很杂 处理效率非常低 不用细看 之后会大改的

import pandas as pd
import jieba
import re
import random

def label2ind(label:pd.Series):
    unique_labels = label.unique()
    return {label: index + 1 for index, label in enumerate(unique_labels)}

def split_text(text, to_Sentences = False):
    text_no_n = text.rstrip()
    result = [t for t in text_no_n.split("\n") if len(t)>0]
    if(to_Sentences):
        text = re.sub('([。！？\?])([^”’])', r"\1\n\2", text)  # 单字符断句符
        #text = re.sub('(\.{6})([^”’])', r"\1\n\2", text)  # 英文省略号
        #text = re.sub('(\…{2})([^”’])', r"\1\n\2", text)  # 中文省略号
        text = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', text)
        text = text.rstrip()
        result.extend([t for t in text.split("\n") if len(t)>0])
    return result

def preprocess_line(line, category, data_list): #for FastText
    try: 
        line = re.sub(r'\n', ' ', line)
        line = re.sub(r'\s+', ' ', line)
        stopwords = list(open(r'data/hit_stopwords.txt','r', encoding='utf-8'))                      
        segs=jieba.lcut(line)
        segs = list(filter(lambda x:x not in stopwords, segs))
        if(len(segs) > 2):
        # __label__1 词语 词语 词语 FastText的格式
            data_list.append("__label__" + str(category) + " "+ " ".join(segs))
    except Exception as e:
        print(e)

def augment_dataset(df, augment_sents = False):
    new_df = pd.DataFrame({'text': [], 'label' : []})
    for i in range(len(df)):
        paras = split_text(df.iloc[i].text, augment_sents)
        new_df = pd.concat([new_df, pd.DataFrame({'text':paras, 'label':[df.iloc[i].label]*len(paras)})])
    return pd.concat([new_df, df])

def generate_FT_dataset(df):
    LABEL_IND = label2ind(df.label)
    new_df = augment_dataset(df)
    dataset = []
    for i in range(len(new_df)):
        preprocess_line(new_df.iloc[i].text, LABEL_IND[new_df.iloc[i].label], dataset)
    random.shuffle(dataset)
    out = open('data/train_data.txt', 'w', encoding='utf-8')
    for dataset in dataset:
        out.write(dataset + "\n")

def text_predict(text):
    line = re.sub(r'\n', ' ', text)
    line = re.sub(r'\s+', ' ', line)
    words = jieba.lcut(line)
    return " ".join(words)
    
if __name__ == '__main__':
    df = pd.read_excel("data/fun.xlsx")
    generate_FT_dataset(df)