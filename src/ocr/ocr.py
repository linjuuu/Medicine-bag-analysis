
'''
    네이버 ocr을 실행하는 클래스 파일입니다.
    
    생성자 파라미터 :
    파일의 확장자명
    
    반환 :
    없음
    
    설명 :
    네이버 ocr을 수행하여 결과물을 저장합니다
    temp_data 폴더에 ocr_response.json 으로 저장됩니다. 
'''


import requests
import uuid
import time
import json

class Ocr:
    def __init__(self,extension):
        # 설정 파일 로드
        with open('config.json') as f:
            self.config = json.load(f)
    
        self.extension = extension

    def execute(self):
        request_json = {
            'images': [
                {
                    'format': self.extension,
                    'name': 'demo'
                }
            ],
            'requestId': str(uuid.uuid4()),
            'version': 'V2',
            'timestamp': int(round(time.time() * 1000))
        }

        payload = {'message': json.dumps(request_json).encode('UTF-8')}
        files = [
            ('file', open(self.config['WARPED_IMAGE_PATH'] + self.extension,'rb'))
        ]
        headers = {
            'X-OCR-SECRET': self.config['SECRET_KEY']
        }

        response = requests.request("POST", self.config['API_URL'], headers=headers, data = payload, files = files)
        
        with open(self.config['OCR_SAVE_PATH'], 'w', encoding='utf-8') as json_file:
            json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
            
        print(f"ocr 결과가 {self.config['OCR_SAVE_PATH']} 경로에 저장되었습니다.")