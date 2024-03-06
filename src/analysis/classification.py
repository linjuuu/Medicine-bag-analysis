'''
    ocr 결과물을 특징별로 분류하는 클래스입니다.
    
    생성자 파라미터 : 
    없음
    
    반환 :
    없음
    
    설명 : 
    ocr 결과를 분석합니다.
    차후 성공할 때마다 붙여넣을 것입니다. 
'''

import json
import re

class Classification : 
    def __init__(self) :
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['IMPORTANT_OCR'], 'r', encoding='utf-8') as json_file:
            self.info = json.load(json_file)
            
  