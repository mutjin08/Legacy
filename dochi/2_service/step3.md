# 템플릿 필터 작성하기
구현하지 않음
# 템플릿 필터 사용하기
구현하지 않음

# 답변 개수 표시
### /workspace/mysite/templates/pybo/question_list.html
질문 목록에 “해당 질문에 달린 답변 개수” 를 표시할 수 있는 기능을 추가
{% if question.answer_set.count > 0 %}
<span>{{ question.answer_set.count }}</span>
{% endif %}
python manage.py runserver 0:80