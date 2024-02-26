'''
    해당 프로그램을 수행하며 생성된 중간 파일들을 삭제하는 클래스입니다.
    
    생성자 파라미터 : 
    입력 이미지 확장자명
    
    반환 :
    없음
    
    설명 : 
    프로그램 수행 중 생성된 워핑 이미지, ocr 응답, ocr 추출 파일 등
    생성된 모든 파일을 삭제합니다. 
'''


import json
import os


class RemoveFile :
    def __init__(self,extension):
        with open('config.json') as f:
            self.config = json.load(f)
        self.extension = extension
    
    def do(self):
        print('\n', '사용한 파일을 모두 삭제하고 프로그램을 종료합니다.')
        
        file_path = self.config['SAVE_PATH'] + self.extension
        try :
            os.remove(file_path)
            print(f"파일 '{file_path}' 삭제 완료")
        except OSError as e:
            print(f"파일 '{file_path}' 삭제 실패: {e}")
        
        file_path = self.config['WARPED_IMAGE_PATH'] + self.extension
        try :
            os.remove(file_path)
            print(f"파일 '{file_path}' 삭제 완료")
        except OSError as e:
            print(f"파일 '{file_path}' 삭제 실패: {e}")
            
        file_path = self.config['OCR_SAVE_PATH']
        try :
            os.remove(file_path)
            print(f"파일 '{file_path}' 삭제 완료")
        except OSError as e:
            print(f"파일 '{file_path}' 삭제 실패: {e}")
        
        file_path = self.config['IMPORTANT_OCR']
        try :
            os.remove(file_path)
            print(f"파일 '{file_path}' 삭제 완료")
        except OSError as e:
            print(f"파일 '{file_path}' 삭제 실패: {e}")