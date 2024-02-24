
'''
    ocr 결과에서 사용할 정보만 추출하는 클래스입니다. 
    
    생성자 파라미터 :
    없음
    
    반환 :
    없음
    
    설명 :
    ocr 결과물을 읽어와서 사용할 정보만을 추출합니다
    사용할 정보는 인식된 텍스트와
    왼쪽 위, 오른쪽 아래 좌표값입니다. 
'''

import json

class ExtractImportantInfo :
    def __init__(self) :
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['OCR_SAVE_PATH'], 'r', encoding='utf-8') as json_file:
            self.response = json.load(json_file)
    
    def extract_column(self) :
        fields = self.response['images'][0]['fields']
        self.important_info = [(field['inferText'], field['boundingPoly']['vertices'][0], field['boundingPoly']['vertices'][2]) for field in fields]
        
        with open(self.config['IMPORTANT_OCR'], 'w', encoding='utf-8') as json_file:
            json.dump(self.important_info, json_file, ensure_ascii=False, indent=4)
            
        print(f"ocr 결과에서 필요한 컬럼만 추출하여 {self.config['IMPORTANT_OCR']} 경로에 저장되었습니다.")