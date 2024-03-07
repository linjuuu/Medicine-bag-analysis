
import json
import re

class Classification:
    def __init__(self):
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['IMPORTANT_OCR'], 'r', encoding='utf-8') as json_file:
            self.info = json.load(json_file)
        
        self.db = ["라베플러스정10mg" , '에소프라졸정40mg' , "가토젠정" , "레바미드정", "애니틴서방정", "모티리톤정_" , "부스론정5mg",
                   "비모보정" , "세페리손정" , "페인리스서방정", "아스피린프로텍트정" , "노페로캡슐"]
        self.medicines = []
            
    def is_medicine_name(self, word):
        if word in self.db :
            return True
        else :
            return False
        
    def is_take_info(self,word):
        # 숫자와 단위를 추출하는 정규 표현식
        pattern = r'(\d+)(정|정씩|캡슐|캡슐씩|회|회당|일|일분)'
        
        # 정규 표현식에 매칭되는 모든 문자열을 찾아서 리스트로 반환
        matches = re.findall(pattern, word)
        
        if len(matches) > 0 :
            return matches
        else :
            return False
        
    def print_result(self):
        for medicine in self.medicines :
            
            medicine_name = ''
            
            take_unit_filter = ['정' , "정씩" , "캡슐" , "캡슐씩" ]
            take_unit = -1
            
            take_number_filter = ['회' , "회씩"]
            take_number = -1
            
            take_days_filter = ['일' , "일분"]
            take_days = -1 
            
            if len(medicine) >= 2 :
                medicine_name = medicine[0]
                
                for info in medicine[1]:
                    
                    if info[1] in take_unit_filter :
                        take_unit = info[0]
                    elif info[1] in  take_number_filter:
                        take_number = info[0]
                    elif info[1] in take_days_filter :
                        take_days = info[0]
                
                print('------------------------')
                print("약이름 : " , medicine_name)
                print("1회 투약량 : " , take_unit)
                print("하루 복용량 : " , take_number)
                print("총 복용일 : " , take_days)
            
                
            
    def do(self):
        # 추후 딕셔너리형으로 바꾸거나 다른 자료형을 사용하는게 어떨지 고민중 
        
        # 하나의 약에 대해 복약정보를 담을 리스트 
        medicine_info = []
        for element in self.info:
            word = element[0]
            
            # 약 이름에 해당되면, 지금까지 복약정보를 담은 리스트를 추가하고, 새로운 리스트 생성 
            if self.is_medicine_name(word) :
                self.medicines.append(medicine_info)
                medicine_info = []
                medicine_info.append(word)
                
            # 복약정보이면 해당 약에 해당하는 리스트에 삽입하기
            take_info = self.is_take_info(word)
            if take_info :
                medicine_info.append(take_info)
                
                
        # 마지막에 기록된 복약정보도 추가하기 
        self.medicines.append(medicine_info)
        print(self.medicines)
        self.print_result()
                
            
c = Classification()
c.do()