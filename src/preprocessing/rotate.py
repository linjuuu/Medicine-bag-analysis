
'''
    이미지의 회전을 감지하고 올바른 방향으로 회전하는 클래스입니다.
    
    생성자 파라미터 :
    파일의 확장자명
    
    반환 :
    없음
    
    설명 :
    ocr을 할 때 회전된 이미지도 잘 동작하는 것을 확인했습니다.
    삭제 예정 
'''


class Rotate :
    def __init__(self, extension) :
        self.extension = extension