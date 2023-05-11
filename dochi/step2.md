# 장고 관리자
//장고 관리자 화면에 접속할 수 있는 슈퍼유저 (superuser) 를 생성
### terminal
python manage.py createsuperuser

//입력하는 내용
Username (leave blank to use 'root'): mutjin08
Email address: mutjin08@gmail.com
Password:
Password (again):

### terminal
python manage.py runserver 0:80


### 관리자 화면 접속
https://mysite-qcyjp.run.goorm.site/admin/
생성한 관리자 계정으로 로그인한다

### 모델 등록
/mysite/pybo/admin.py
/mysite/pybo/models.py
admin.py 파일에 models.py 에서 생성한 모델을 등록한다

"""
from django.contrib import admin
from .models import Question

admin.site.register(Question)
"""
//admin.site.register로 Question 모델을 등록했다. 그리고 장고 관리자 화면을 갱신해 보면 Question 이 추가된 것을 확인할 수 있다.
//이제 Question 객체를 관리자 화면에서 신규로 생성할 수 있다.

### 모델 검색
/mysite/pybo/admin.py
/mysite/pybo/models.py
admin.py 파일에 models.py 에서 생성한 모델 객체를 검색할 수 있는 기능을 추가한다

"""
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
"""
//admin.site.register로 Question 모델을 등록했다. 그리고 장고 관리자 화면을 갱신해 보면 Question 이 추가된 것을 확인할 수 있다.
//이제 관리자 화면에서 제목 (subject) 으로 Question 객체를 검색할 수 있다.
