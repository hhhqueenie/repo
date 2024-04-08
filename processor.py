import numpy as np
import fasttext
from model import data_preprocess, train
import redisUse

#writer_list = ["4680", "4201", "1678","威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

label2cate = {'__label__1':'Crowley1678', '__label__2' : 'Crowley4680', '__label__3':'Aziraphale4201'}

try:
    classifier = fasttext.load_model('data/classifier.model')
except ValueError:
    classifier = train.fit('data/train_data.txt')
    classifier.save_model('data/classifier.model')
    
def do(text):
    redisUse.addUserInput(text)
    original = text
    text = data_preprocess.text_predict(text)
    pred = classifier.predict(text, k = -1)
    #s = f"你的文章有 {round(pred[1][0], 2)} 的概率像 {label2cate[pred[0][0]]}" +/n
    result = []
    #original = text if len(text) < 50 else "太长啦，不显示啦 QwQ "
    redisUse.recordResult(label2cate[pred[0][0]])
    for i in range(3):
        result.append(f"有 {round(pred[1][i] * 100, 2)} % 的概率像 {label2cate[pred[0][i]]}")
    
    #result.append(original)
    result.append(original)

    # print("user input as follows: ")
    # print(redisUse.getAllUserInputs())
    # print("total frequency as follows: ")
    # print(redisUse.getAllFrenquency())

    return result