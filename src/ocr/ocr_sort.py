'''
    ocr에서 사용할 정보들을 x,y 좌표를 기준으로 정렬하는 클래스입니다.
    
    생성자 파라미터 :
    없음
    
    반환 :
    없음
    
    설명 :
    복약정보 분류를 할 때, 불확실한 값은 좌표값을 이용해 사용할 가능성이 있습니다.
    x 오름차순, y오름차순을 각각 저장하였습니다.
'''


import json

class OcrSort :
    def __init__(self) :
        with open('config.json') as f:
            self.config = json.load(f)
        
        with open(self.config['IMPORTANT_OCR'], 'r', encoding='utf-8') as json_file:
            self.response = json.load(json_file)
    
    def sort(self):
        sorted_data_x = sorted(self.response, key=lambda x: x[1]["x"])
        with open(self.config['IMPORTANT_OCR_X'], 'w', encoding='utf-8') as json_file:
            json.dump(sorted_data_x, json_file, ensure_ascii=False, indent=4)
        
        sorted_data_y = sorted(self.response, key=lambda x: x[1]["y"])
        with open(self.config['IMPORTANT_OCR_Y'], 'w', encoding='utf-8') as json_file:
            json.dump(sorted_data_y, json_file, ensure_ascii=False, indent=4)
        
ocr_sort = OcrSort()
ocr_sort.sort()