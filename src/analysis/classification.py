'''
    ocr 결과물을 특징별로 분류하는 클래스입니다.
    
    생성자 파라미터 : 
    없음
    
    반환 :
    없음
    
    설명 : 
    ocr 결과들을 모두 순회하며 분류 함수에 넣습니다.
    숫자인지, 약 이름인지, 특징명인지, 특징값인지 분류하고 있습니다.
    계속 추가할 계획입니다. 
'''

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
                        '일투여횟수','일투여','일','투여','횟수','투여일수'
                        '총투약일수','총투약','총','투약','일수','투약일수'
                        '총투약횟수','횟수','투약횟수'
                        '아침','점심','저녁','취침전','의사지시대로'
                        '식전','식후','식후30분','식후즉시','식전30분','식사 상관없이','식사','공복','표시대로'
                        '복용','약품명','복약안내'
                        ]
        
        if word in feacher_name :
            return True
        else:
            return False
        
    def is_feature_value(self,word):
        # 정규표현식 -> 해당 단어로 끝나거나 포함된 것을 리턴하도록 하기
        pattern = r'^\d+.*(정|캡슐|일|분|일분|회|포|시간|시간마다)\b'
        
        # 정규표현식을 이용해 T/F 리턴
        return bool(re.match(pattern, word))

    def classify(self) :
        print('\n','단어 분류를 시작합니다.')
        for element in self.info :
            word = element[0]
            
            # if self.is_num(word) :
            #     print("숫자 : " ,  word)
                
            if self.is_drug_name(word) :
                print("약이름 : ",word)
                
            if self.is_feature_name(word) :
                self.feature_sequence.append(word)
            
            if self.is_feature_value(word) :
                print("복약 특징값 : " , word)
                
        
        print("복약 특징 순서 : ",self.feature_sequence)