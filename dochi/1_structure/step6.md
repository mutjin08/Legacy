# 스태틱
디자인을 적용하기 위해서는 스타일시트 (stylesheet, CSS 파일) 를 사용해야 한다.
스타일시트 파일은 장고의 스태틱 디렉터리에 저장해야 한다.

### /workspace/mysite/config/settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]