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
        self.taking_info = []
    
    
    #숫자 (정수,실수) 인지 판단
    def is_num(self, word):
        # 숫자를 나타내는 정규표현식
        number_pattern = r'^[-+]?\d*\.?\d+$'
        
        # 입력된 문자열이 숫자로만 이루어져 있는지 판단
        if re.match(number_pattern, word):
            return True
        else:
            return False
    
    # 약 이름인지 판단 (db 쿼리로 변경해야함)  
    def is_drug_name(self,word):
        db = ['러키펜정','레스탐정', "고려세파클러캡슐",
              '인데놀정10mg', '인데놀정', "록스펜정","엑소페린정50mg",
              '세푸로틸정','덱스핀정','레미스타정','목클린캡슐200밀리그램','베포캄정','비알코시럽',
              '록스펜정','엑소페린정50mg'
              ]
        
        if word in db :
            return True
        else :
            return False
    
    # 특징명 중에 하나인지 판별
    def is_feature_name(self,word):
        feacher_name = [
                        '1회 투약량', '투약량',
                        '일투여횟수','일투여','투여','횟수','투여일수'
                        '총투약일수','총투약','투약','일수','투약일수'
                        '총투약횟수','횟수','투약횟수'
                        ]
        
        # 특징명이지만, 포함할지 고민이 되는 것들
        # 현재 feature_name 으로만 하는건 하드코딩에 가까운 상태...
        # other_feature = [
        #                 '1회','일','총'
        #                 '아침','점심','저녁','취침전','의사지시대로'
        #                 '식전','식후','식후30분','식후즉시','식전30분','식사 상관없이','식사','공복','표시대로'
        #                 '복용'
        #                 ]
        
        if word in feacher_name :
            return True
        else:
            return False
    
    # 특징값 중에 하나인지 판별 
    def is_feature_value(self,word):
        # 정규표현식 -> 해당 단어로 끝나거나 포함된 것을 리턴하도록 하기
        pattern = r'^\d+.*(정|캡슐|일|분|일분|회|포|시간|시간마다)\b'
        
        #포함할까 고민이 되는 특징값들
        #pattern = r'^\d+.*(시간|시간마다)\b'
        
        # 정규표현식을 이용해 T/F 리턴
        return bool(re.match(pattern, word))



    # 분류기를 실행하는 함수
    def classify(self) :
        print()
        print('단어 분류를 시작합니다.')
        
        # 우선 해당 약 봉투에서 특징명의 순서를 파악하기
        for element in self.info :
            word = element[0]

            if self.is_feature_name(word) :
                    self.feature_sequence.append(word)
        
        if len(self.feature_sequence) < 3 :
            print("특징명 추출 실패 가능성, 서브 키워드 검사 필요")
        
        print("복약 값 순서 : ", self.feature_sequence)
        print()
        
        
        taking_info = []
        for element in self.info :
            word = element[0].split('[')[0]
            
            
            #약 이름이라면 
            if self.is_drug_name(word) :
                self.taking_info.append(taking_info)
                taking_info = []
                taking_info.append(word)
            
            #복약 정보라면
            elif self.is_feature_value(word):
                taking_info.append(word)     
            elif self.is_num(word):
                taking_info.append(word)
                
        self.taking_info.append(taking_info)
        for i in range(1, len(self.taking_info)):
            print(self.taking_info[i])
            
c = Classification()
c.classify()