#input zip file을 사용 후 삭제
#input이 들어오는 폴더를 아예 비우기
import os

def DeleteAll (filePath):
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            os.remove(filePath)
        
    else: return 'Input file error'
    