'''
    이미지의 워핑을 수행하는 클래스입니다.
    
    입출력 :
    입력 => 파일의 확장자명
    출력 => 없음
    
    설명 :
    파일 전처리를 통해 저장한 이미지를 불러옵니다. 
    해당 이미지에서 4개의 지점을 클릭하여 좌표값을 가져옵니다.
    해당 좌표값을 기준으로 워핑을 수행합니다.
    그 후 temp_data 에 warped_image 라는 이름으로 워핑된 이미지를 저장합니다. 
'''


import cv2
import numpy as np

class WarpingBy4points :
    def __init__(self, extension) :
        self.extension = extension 
        self.image = cv2.imread("temp_data/input_image." + extension , cv2.IMREAD_COLOR)
    
    #선택하는 지점의 좌표를 가지고 오기 위한 마우스 콜백 함수
    def mouse_callback(self , event, x, y, flags,param):
        points = self.points
        image = param[0]
        
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append([x, y])

            # 클릭한 지점에 원 그리기
            radius = 30  
            color = (255, 255, 0)  
            thickness = -1  
            cv2.circle(image, (x, y), radius, color, thickness)
            cv2.imshow("original", image)
    
    #워핑을 수행할 4개의 지점을 추출하는 함수
    def get_points(self):
        self.points = []
        image = self.image.copy()
        
        cv2.imshow("original", image)
        cv2.setMouseCallback("original", self.mouse_callback , [image])
        
        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or len(self.points) == 4:
                break
        cv2.destroyAllWindows()  
    
    #선택된 4개의 지점을 토대로 워핑을 수행하는 함수 
    def warping(self) :
        src_points = np.array(self.points, dtype=np.float32)
        dst_points = np.array([[0, 0], [self.image.shape[1], 0], [self.image.shape[1], self.image.shape[0]], [0, self.image.shape[0]]], dtype=np.float32)
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        dst = cv2.warpPerspective(self.image, matrix, (self.image.shape[1], self.image.shape[0]))
        
        save_path = "temp_data/warped_image." + self.extension
        cv2.imwrite(save_path, dst)
        print(f"워핑된 이미지가 {save_path} 경로에 저장되었습니다.")