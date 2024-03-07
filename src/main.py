from input_image.file_processing import FilePreprocessing
from preprocessing.warping_by_4points import WarpingBy4points
from preprocessing.detect_border import DetectBorder
from ocr.ocr import Ocr
from ocr.extract_important_info import ExtractImportantInfo
from analysis.classification import Classification
from finish.remove_file import RemoveFile

INPUT_IMAGE_PATH = "input_images/hardexception.png" 

if __name__ == "__main__" :
    
    #------------------------------------------------------
    #파일 전처리 객체 생성
    file_preprocessing = FilePreprocessing(INPUT_IMAGE_PATH) 
    
    #파일을 저장하고, 확장자명 리턴 
    extension = file_preprocessing.save_image() 
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    #이미지 전처리 - 객체 생성
    warping_by_4points = WarpingBy4points(extension)
    
    #이미지에서 워핑을 수행할 4개의 지점 선택
    warping_by_4points.get_points()
    
    #이미지 워핑 수행 
    warping_by_4points.warping()
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    # 이미지 전처리 - 테두리 검출 객체 생성 (실패)
    # detect_border = DetectBorder("jpeg")
    # detect_border.detect_border()
    #------------------------------------------------------
    
        

    #------------------------------------------------------
    #OCR - ocr 객체 생성
    ocr = Ocr(extension)
    ocr.execute()
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    #OCR - 중요 정보 추출 객체 생성
    extract_important_info = ExtractImportantInfo()
    extract_important_info.extract_column()
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    # analysis - 분류 객체 생성
    classification = Classification()
    classification.classify()
    #------------------------------------------------------
    
    
    
    #------------------------------------------------------
    # finish - 종료 후 중간 생성 파일 삭제 객체 생성
    # remove_file = RemoveFile(extension)
    # remove_file.do()
    #------------------------------------------------------