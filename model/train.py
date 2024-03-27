import fasttext

def fit(train_set_path):
    return fasttext.train_supervised(input=train_set_path, wordNgrams=2, epoch=50, lr=0.1, dim=300)

if __name__ == '__main__':
    classifier = fit('data/train_data.txt')
    result = classifier.test('data/train_data.txt')
    print('P@1:', result[1])
    print('R@1:', result[2])
    print('Number of examples:', result[0])
    classifier.save_model('data/a.model')