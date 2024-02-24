'''
    파일 전처리를 수행하는 클래스입니다.
    
    생성자 파라미터 : 
    이미지 경로
    
    반환 :
    파일의 확장자명
    
    설명 : 
    현재는 파일의 경로값을 입력받고, temp_data에 이미지를 저장하고 있습니다
    추후 파일에 대한 전처리 필요성이 생길 것 같아 클래스로 정의했습니다.  
'''

import os
import cv2
import json

class FilePreprocessing :
    def __init__(self, image_path) :
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.extension = image_path.split('.')[-1] 
    
    #이미지를 저장하는 함수
    def save_image(self):
        with open('config.json') as f:
            config = json.load(f)
        save_path = config['SAVE_PATH'] + self.extension
        
        cv2.imwrite(save_path, self.image)
        print(f"이미지가 {save_path} 경로에 저장되었습니다.")
        return self.extension