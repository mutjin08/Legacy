# 질문 목록과 질문 상세 기능을 구현
질문 목록 ‑ 등록한 질문들을 게시물 목록으로 조회하는 기능
질문 상세 ‑ 게시물 목록 중 한 건의 데이터를 상세하게 조회하는 기능

### terminal
python manage.py migrate
python manage.py runserver 0:80

### 실행 url
https://mysite-qcyjp.run.goorm.site/pybo/

# 질문 목록

## /mysite/pybo/views.py
from django.shortcuts import render
from .models import Question

def index(request):
    question_list = Question.bojects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'pybo/question_list.html', context)

### Question.objects.order_by('-create_date')
//질문 목록 데이터 얻기
//order_by('-create_date')는 작성일시 역순으로 정렬하라는 의미이다.
//'-' 기호가 붙어 있으면 역방향, 없으면 순방향 정렬을 의미한다.
//게시물은 보통 최신순으로 보기 때문에 작성일시의 역순으로 정렬했다.

### render 함수
//파이썬 데이터를 템플릿에 적용하여 HTML 로 반환하는 함수이다.
//위에서 사용한 render 함수는 질문 목록으로 조회한 question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML 을 생성한후 리턴한다. 
//여기서 사용된 pybo/question_list.html과 같은 파일을 템플릿 (Template) 이라고 부른다. 
//템플릿 파일은 HTML 파일과 비슷하지만 파이썬 데이터를 읽어서 사용할수 있는 HTML 파일이다.

## templates dir 생성
### /workspace/mysite/templates
템플릿 파일을 저장할 디렉터리 생성


### /workspace/mysite/config/settings.py
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""


### /workspace/mysite/pybo/templates
DIRS에 설정한 디렉터리 외에도 앱 디렉터리 바로 하위에 있는 templates 디렉터리도 템플릿 디렉터리로 인식한다.
앱 (App) 디렉터리 하위에 템플릿 디렉터리를 두는 방법을 권장하지 않는다. 왜냐하면 하나의 웹 사이트에서 여러 앱을 사용할 때 여러 앱의 화면을 구성하는 템플릿은 한 디렉터리에 모아관리하는 편이 여러모로 좋기 때문이다.

## 템플릿 태그

### /workspace/mysite/templates/pybo/question_list.html

### 분기
### 반복
### 객체 출력

# 질문 상세

### /workspace/mysite/pybo/urls.py
### /workspace/mysite/pybo/views.py
### /workspace/mysite/templates/pybo/question_detail.html

## 오류 페이지
500 error 보다는 404 error가 낫기 때문에
### /workspace/mysite/pybo/views.py