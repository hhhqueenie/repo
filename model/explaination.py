# -*- coding: utf-8 -*-

from lime.lime_text import LimeTextExplainer
import numpy as np
import re
import json

class Explainer():
    def __init__(self, classifier):
        self.classifier = classifier
        label2ind = json.load(open('data/files/label2ind.json', 'r', encoding='utf-8'))
        self.ind2label = {value: key for key, value in label2ind.items()}

    def predict_proba(self, texts):
        labels, probabilities = self.classifier.predict(texts, k=len(self.classifier.get_labels()))
        mapped_labels = [[self.ind2label[label] for label in label_list] for label_list in labels]
        mapped_probabilities = [dict(zip(mapped_label_list, prob_list)) for mapped_label_list, prob_list in zip(mapped_labels, probabilities)]
        return np.array([[prob_dict.get(class_name, 0) for class_name in self.ind2label.values()] for prob_dict in mapped_probabilities])

    def split_rule(self, text):
        sentences = re.split('(。|！|\!|\.|？|\?)',text)
        new_sents = []
        for i in range(int(len(sentences)/2)):
            sent = sentences[2*i] + sentences[2*i+1]
            new_sents.append(sent)
        return new_sents

    def get_explaination(self, text): # text: need to be preprocessed and cut before passing in
        model = LimeTextExplainer(split_expression=self.split_rule, class_names=list(self.ind2label.values()))
        exp = model.explain_instance(text, self.predict_proba, num_features=1000, top_labels=3)
        return exp
    
    
    def get_explaination_with_positions(self, text):
        """
        Args:
            text: str

        Returns:
            text: str 
                This text is preprocessed, might be different from the user's original input. Please use this text to display the result.
            result: { (start_pos, end_pos) : [(author1, score1), (author2, score2), (author3, score3)] }
        """
        if(len(self.split_rule(text)) <= 1):
            return text.replace(' ', ''), None
        
        exp = self.get_explaination(text)
        exp_map = exp.as_map()
        
        text = text.replace(' ', '')
        sentences = self.split_rule(text)

        result = {}

        for key in exp_map.keys():
            indexes_scores = exp_map[key]
            for i, score in indexes_scores:
                author = self.ind2label[f'__label__{key}']

                sentence = sentences[i]
                start_pos = text.find(sentence)
                end_pos = start_pos + len(sentence)
                score = round(score * 100, 2)
                
                try:
                    result[(start_pos, end_pos)].append((author, score))
                except KeyError:
                    result[(start_pos, end_pos)] = [(author, score)]
        result = dict(sorted(result.items(), key=lambda item: item[0][0])) # sort by sentence position
        return text, result