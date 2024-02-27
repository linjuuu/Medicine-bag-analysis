'''
    워핑하고, 테두리 검출을 하려는 파일입니다. 
    그러나 아직 구현에 실패했습니다.
    
    생성자 파라미터 : 
    확장자명
    
    반환 :
    없음
    
    설명 : 
    전체 사진을 ocr 하는 것보다 복약에 관련된 영역만을 추출하여 하는 것이 정확도가 높습니다
    그래서 영역을 분리하는 것이 필요한데, 테두리 검출이 어려운 상태입니다.
'''


import cv2
import json

class DetectBorder :
    def __init__(self, extension):
        self.extension = extension
        
        with open('config.json') as f:
            self.config = json.load(f)
            
        self.image = cv2.imread(self.config['SAVE_PATH'] + extension , cv2.IMREAD_COLOR)
    
    def detect_border(self):
        image = self.image
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        
        edge = cv2.Canny(gray, 100, 100)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        adaptive_threshold= cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        # 컨투어 찾기
        contours, hierachy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # 컨투어 면적이 큰 순으로 정렬
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
        
        for i in range(len(sorted_contours)):
            contour = sorted_contours[i]
            
            # 근사 컨투어 계산을 위한 0.01의 오차 범위 지정 
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            cv2.drawContours(image, [contour], -1, (0,255,0), 3)
            
            
        # 결과 출력
        cv2.imshow('contour', image)
        cv2.waitKey()
        cv2.destroyAllWindows()