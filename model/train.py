import fasttext
import pandas as pd

def fit(train_set_path):
    return fasttext.train_supervised(input=train_set_path, wordNgrams=2, epoch=100, lr=0.1, dim=300)

def predict_formated_results(text, classifier):
    labels, probs = classifier.predict(text, k = 3)
    df = pd.read_csv('data/authors.csv', encoding='utf-8')
    result = []
    for i in range(3):
        id = labels[i][9:]        
        row = df[df['id'] == int(id)]

        if row.empty:
            print(f"No data found for id {id}")
            break
        
        name = row['full_name'].values[0]
        ori_name = row['ori_name'].values[0]
        works = row.iloc[:, -3:].values.tolist()[0]
        works = [work for work in works if pd.notna(work)]
        result.append([name, ori_name, probs[i], works, id])
    return result

if __name__ == '__main__':
    classifier = fit('data/files/train.txt')
    result = classifier.test('data/files/train.txt')
    print('P@1:', result[1])
    print('R@1:', result[2])
    print('Number of examples:', result[0])
    classifier.save_model('data/classifier.model')