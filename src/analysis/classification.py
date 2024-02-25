import json
import re

class Classification : 
    def __init__(self) :
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['IMPORTANT_OCR'], 'r', encoding='utf-8') as json_file:
            self.info = json.load(json_file)
    
    def is_num(self, word):
        # 숫자를 나타내는 정규표현식
        number_pattern = r'^[-+]?\d*\.?\d+$'
        
        # 입력된 문자열이 숫자로만 이루어져 있는지 판단
        if re.match(number_pattern, word):
            return True
        else:
            return False
        

    def classify(self) :
        
        for element in self.info :
            word = element[0]
            
            if self.is_num(word) :
                print("숫자 : " ,  word)
            
            
            
            

classification = Classification()
classification.classify()