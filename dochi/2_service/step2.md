# 페이징
우리가 구현한 질문 목록은 현재 페이징 처리가 안되기 때문에 게시물 300 개를 작성하면 한 페이지에 300개의 게시물이 모두 표시된다. 
페이징 (Paging) 을 적용하여 이 문제를 해결해 보자.

## 데이터 생성
페이징을 구현하기 전에 페이징을 테스트할 수 있을 정도로 충분한 데이터를 장고 shell에서 300개 생성하자.

# terminal
python manage.py shell
from pybo.models import Question
from django.utils import timezone
for i in range(300):
    q = Question(subject='테스트게시물 생성:[%03d]' %i, content='내용은없지롱~', create_date=timezone.now())
    q.save()
python manage.py runserver 0:80


## Paginator
Paginator 클래스를 사용하여 다음과 같이 index 함수에 페이징 기능을 적용해 보자.

### /workspace/mysite/pybo/views.py
index(request) 수정하기

## 템플릿에 페이징 적용하기
### /workspace/mysite/templates/pybo/question_list.html