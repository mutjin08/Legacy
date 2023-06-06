#input zip파일 압축을 풀고
#numpy array로 변환하는 함수
import os

def get_input():
    input_arr = os.chdir('../media/image')
    path_input = '../media/image/'+input_arr[0]
    extract_to = '../media/image'
    
    import zipfile
    with zipfile.ZipFile(path_input, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    input_path = '../media/image/npz/'+input_arr[0]    
    
    return input_path