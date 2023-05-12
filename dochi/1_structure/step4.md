# url 별칭
템플릿에 사용된 URL 의 하드코딩을 없애려고 한다

### /workspace/mysite/templates/pybo/question_list.html

URL 링크의 구조가 자주 변경된다면 템플릿에서 사용한 모든 URL 들을 일일이 찾아가며 수정해야 하는 리스크가 발생한다. 
이러한 문제점을 해결하기 위해서는 해당 URL 에 대한 실제 링크 대신 링크의 주소가 1:1 매핑되어 있는 별칭을 사용해야 한다.


<li><a href="/pybo/{{ question.id }}/">{{ question.subject }}</a></li>
http://localhost:8000/pybo/question/2 
http://localhost:8000/pybo/2/question


### /workspace/mysite/pybo/urls.py
path('<int:question_id>/', views.detail)
-> path('<int:question_id>/', views.detail, name='detail')

### /workspace/mysite/templates/pybo/question_list.html
<a href="/pybo/{{ question.id }}/">
-> <a href="{% url 'detail' question_id=question.id %}">

# url 네임스페이스 추가
현재는 pybo 앱 하나만 사용중이지만 pybo 앱 이외의 다른 앱이 프로젝트에 추가 될 수도 있을 것이다. 
이런 경우 서로 다른 앱에서 동일한 URL 별칭을 사용하면 중복이 발생할 것이다.
이 문제를 해결하려면 pybo/urls.py 파일에 네임스페이스를 의미하는 app_name 변수를 지정해야 한다. 

### mysite/pybo/urls.py
app_name = 'pybo'

### /workspace/mysite/templates/pybo/question_list.html
<a href="{% url 'detail' question_id=question.id %}">
-> <a href="{% url 'pybo:detail' question_id=question.id %}">