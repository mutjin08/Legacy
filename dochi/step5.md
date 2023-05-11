# 데이터 저장

## 답변등록 폼
답변을 등록하는 기능
질문 상세 템플릿에 답변을 저장할 수 있는 폼 (form) 을 추가
 
### /workspace/mysite/templates/pybo/question_detail.html
<form action="{% url 'pybo:answer_create' question_id=question.id %}" method="post">

## url 매핑
### /workspace/mysite/pybo/urls.py
path('answer/create/<int:question_id>/', views.answer_create, name="answer_create")

## 뷰 함수
### /workspace/mysite/pybo/views.py

"""
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)
""" 
답변을 생성한 후 질문 상세 화면을 다시 보여주기 위해 redirect 함수를 사용했다. 
redirect 함수는 페이지 이동을 위한 함수이다. 
pybo:detail 별칭에 해당하는 페이지로 이동하기 위해 redirect 함수를 사용했다. 
그리고 pybo:detail별칭에 해당하는 URL 은 question_id 가 필요하므로 question.id를 인수로 전달했다.