import fasttext

def fit(train_set_path):
    return fasttext.train_supervised(input=train_set_path, wordNgrams=2, epoch=100, lr=0.1, dim=300)

if __name__ == '__main__':
    classifier = fit('data/files/train.txt')
    result = classifier.test('data/files/train.txt')
    print('P@1:', result[1])
    print('R@1:', result[2])
    print('Number of examples:', result[0])
    classifier.save_model('data/classifier.model')