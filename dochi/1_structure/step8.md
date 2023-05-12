# 폼
폼은 쉽게 말해 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스이다. 
폼은 필수 파라미터의 값이 누락되지 않았는지, 파라미터의 형식은 적절한지 등을 검증할 목적으로 사용한다





# 질문 등록하기

## 버튼 만들기
### /workspace/mysite/templates/pybo/question_list.html
<button type="button" onclick="location.href='{% url 'pybo:question_create' %}'">질문 등록하기</button>
 
## URL 매핑
### /workspace/mysite/pybo/urls.py
path('question/create/', views.question_create, name='question_create')

## 폼
### /workspace/mysite/pybo/forms.py

## 뷰 함수
### /workspace/mysite/pybo/views.py

## 템플릿
### mysite/templates/pybo/question_form.html

## GET과 POST
### /workspace/mysite/templates/base.html
### /workspace/mysite/pybo/views.py

# 오류 표시하기
### /workspace/mysite/templates/pybo/question_detail.html
from: <!-- 오류표시 start>
to: <!-- 오류표시 end>