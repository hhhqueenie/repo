import fasttext
from model import data_processor, train
import redisUse

#writer_list = ["4680", "4201", "1678","威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

try:
    classifier = fasttext.load_model('data/classifier.model')
except ValueError:
    classifier = train.fit('data/train_data.txt')
    classifier.save_model('data/classifier.model')
    
def do(text):
    redisUse.addUserInput(text)
    original = text
    text = data_processor.text_predict(text)
    pred = train.predict_formated_results(text, classifier)
    result = []
    #redisUse.recordResult(pred[0][1])
    for i in range(3):
        result.append(f"{round(pred[i][2] * 100, 2)} % {pred[i][0]}")
        result.append(f"这位作者的参考作品有：{' '.join([f'《{work}》' for work in pred[i][3]])}")
    
    result.append(original)
    pred.append(original)

    # print("user input as follows: ")
    # print(redisUse.getAllUserInputs())
    # print("total frequency as follows: ")
    # print(redisUse.getAllFrenquency())

    return pred