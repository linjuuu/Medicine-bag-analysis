from input_image.file_processing import FilePreprocessing
from preprocessing.warping_by_4points import WarpingBy4points
from preprocessing.rotate import Rotate

INPUT_IMAGE_PATH = "input_images/sample1.jpeg" 

if __name__ == "__main__" :
    
    #------------------------------------------------------
    #파일 전처리 객체 생성
    file_preprocessing = FilePreprocessing(INPUT_IMAGE_PATH) 
    
    #파일을 저장하고, 확장자명 리턴 
    extension = file_preprocessing.save_image() 
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    #이미지 전처리 - 회전 객체 생성
    rotate = Rotate(extension)
    
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    #이미지 전처리 - 객체 생성
    warping_by_4points = WarpingBy4points(extension)
    
    #이미지에서 워핑을 수행할 4개의 지점 선택
    warping_by_4points.get_points()
    
    #이미지 워핑 수행 
    warping_by_4points.warping()
    #------------------------------------------------------