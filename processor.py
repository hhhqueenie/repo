import numpy as np
import fasttext
from model import data_preprocess, train

writer_list = ["4680", "4201", "1678","威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

label2cate = {'__label__1':'1678', '__label__2' : '4680', '__label__3':'4201'}

try:
    classifier = fasttext.load_model('data/classifier.model')
except ValueError:
    classifier = train.fit('data/train_data.txt')
    classifier.save_model('data/classifier.model')
    
def do(text):
    text = data_preprocess.text_predict(text)
    pred = classifier.predict(text, k = -1)
    s = f"你的文章有 {round(pred[1][0], 2)} 的概率像 {label2cate[pred[0][0]]}"
    return s
