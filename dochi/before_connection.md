# 수행완료된 작업
payments.html 작성
payments.html url
# 수행해야 할 작업
payments.html 페이지 표시

# 연결하기
### /workspace/mysite/templates/pybo/question_list.html
    <div class="col-6">
        <a href="{% url 'pybo:question_modelcreate' %}" class="btn btn-primary">모델 생성하기</a>
    </div>

### /workspace/mysite/pybo/urls.py
    # model
    path('question/modelcreate/', question_views.question_modelcreate, name='question_modelcreate'),

### /workspace/mysite/pybo/views/question_views.py
@login_required(login_url='common:login')
def question_modelcreate(request):