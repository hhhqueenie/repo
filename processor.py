import fasttext
from model import data_processor, train, explaination
import redisUse

#writer_list = ["4680", "4201", "1678","威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

try:
    classifier = fasttext.load_model('data/classifier.model')
except ValueError:
    classifier = train.fit('data/train_data.txt')
    classifier.save_model('data/classifier.model')
    
def do(text):
    '''
    pred: [[name, ori_name, probs[i], works, id]*3, valid text, exp]
    exp: { (start_pos, end_pos) : [(author1, score1), (author2, score2), (author3, score3)] }
    '''
    redisUse.addUserInput(text)
    original = text
    text = data_processor.text_predict(text)
    pred = train.predict_formated_results(text, classifier)
    #redisUse.recordResult(pred[0][1])

    explainer = explaination.Explainer(classifier)
    valid_text, exp = explainer.get_explaination_with_positions(text)

    if(exp is None):
        exp = {(0, len(valid_text)): [(pred[i][0], round(pred[i][2] * 100, 2)) for i in range(3)]}

    pred.append(valid_text)
    pred.append(exp)

    # print("user input as follows: ")
    # print(redisUse.getAllUserInputs())
    # print("total frequency as follows: ")
    # print(redisUse.getAllFrenquency())

    return pred