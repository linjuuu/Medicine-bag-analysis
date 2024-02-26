import json
import re

class Classification : 
    def __init__(self) :
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['IMPORTANT_OCR'], 'r', encoding='utf-8') as json_file:
            self.info = json.load(json_file)
            
        self.feature_sequence = []
    
    def is_num(self, word):
        # 숫자를 나타내는 정규표현식
        number_pattern = r'^[-+]?\d*\.?\d+$'
        
        # 입력된 문자열이 숫자로만 이루어져 있는지 판단
        if re.match(number_pattern, word):
            return True
        else:
            return False
        
    def is_drug_name(self,word):
        db = ['인데놀정10mg', '인데놀정', '러키펜정','레스탐정']
        
        if word in db :
            return True
        else :
            return False
    
    def is_feature_name(self,word):
        feacher_name = ['1회 투약량', '1회', '투약량',
                        '일투여횟수','일투여','일','투여','횟수',
                        '총투약일수','총투약','총','투약','일수',
                        '총투약횟수','횟수'
                        ]
        
        if word in feacher_name :
            return True
        else:
            return False
        
    def is_feature_value(self,word):
        # 정규표현식 패턴: '정' 또는 '캡슐'로 끝나거나, '정' 또는 '캡슐'을 포함하는 단어
        pattern = r'^\d+.*(정|캡슐|일|분|일분|회|시간|시간마다)\b'
        
        # 정규표현식과 매치되는지 검사하여 결과 반환
        return bool(re.match(pattern, word))

    def classify(self) :
        
        for element in self.info :
            word = element[0]
            
            if self.is_num(word) :
                print("숫자 : " ,  word)
                
            if self.is_drug_name(word) :
                print("약이름 : ",word)
                
            if self.is_feature_name(word) :
                self.feature_sequence.append(word)
            
            if self.is_feature_value(word) :
                print("복약 특징값 : " , word)
                
        
        print("복약 특징 순서 : ",self.feature_sequence)