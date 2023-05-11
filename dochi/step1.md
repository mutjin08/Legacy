# 초기 설정
mysite/mysite -> mysite/config
(settings.py, urls.py, wsgi.py. manage.py)

# terminal

python manage.py migrate
python manage.py runserver 0:80

django-admin startapp pybo

# mysite/pybo/models.py에 모델 작성하기

### TABLE
subject
content
create_date

question
content
create_date

### models.py

from django.db import models

class Question(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    created_date=models.DateTimeField()

class Answer(models.Model):
    subject=models.ForeignKey(Question, on_delete=models.CASCADE)
    content=models.TextField()
    created_date=models.DateTimeField()

//on_delete=models.CASCADE 의 의미: Question이 삭제되면, Answer도 삭제된다

# terminal
python manage.py makemigrations
python manage.py migrate

//새로운 model이 생성되면 makemigrations->migrate
//makemigrations 하면 '/mysite/pybo/migrations/__pycache__/0001_initial.cpython-37.pyc' 생성된다

python manage.py sqlmigrate pybo 0001
//실행되는 query문을 terminal에서 볼 수 있다

# 모델 사용해보기
//refresh
//일반적인 '파이썬 shell'이 아닌 '장고 shell'에서 실행할 수 있다

python manage.py makemigrations
python manage.py migrate
python manage.py shell
from pybo.models import Question, Answer
from django.utils import timezone



//exit django shell
[ctrl]+[z]
exit()



## 생성 terminal
//첫번째 Question객체 q를 생성해서 저장한다
q=Question(subject='일번질문이다', content='고순이는얼마나귀엽니', create_date=timezone.now())
q.save()

//모든 모델에 대해 pk는 id이다. auto incremet임을 확인할 수 있다
q.id

//두번째 Question객체 q를 생성해서 저장하고, pk인 id를 확인한다
q=Question(subject='일번질문이다', content='고순이는얼마나귀엽니', create_date=timezone.now())
q.save()
q.id




## Question 조회 terminal
Question.objects.all()
//result: <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>


//model.py에 __str__ 메서드를 추가하면 제목(subject)을 표시할 수 있다
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject
        

Question.objects.all()
//result: <QuerySet [<Question: 일번질문이다>, <Question: 일번질문이다>]>



# Question.objects.filter(id)
//다건을 return 하기 때문에 'QuerySet이' return된다

Question.objects.filter(id=1)
//result: <QuerySet [<Question: 일번질문이다>]>

Question.objects.filter(id=3)
//result: <QuerySet []>




# Question.objects.get
//한 건을 return 하기 때문에 'Question 모델 객체'가 return된다

Question.objects.get(id=1)
//result: <Question: 일번질문이다>

Question.objects.get(id=3)
//error: DoesNotExist: Question matching query does not exist.




# Question.objects.filter(문자열 포함)
//다건을 return 하기 때문에 'QuerySet이' return된다

Question.objects.filter(subject__contains='질문')
//result: <QuerySet [<Question: 일번질문이다>, <Question: 일번질문이다>]>

Question.objects.filter(subject__contains='문제')
//result: <QuerySet []>






## Question 수정 terminal
q=Question.objects.get(id=2)
q
q.subject='이번질문이다'
q.save()
q




## Question 삭제 terminal
q=Question.objects.get(id=1)
q.delete()
//result: (1, {'pybo.Answer': 0, 'pybo.Question': 1})
//Question 모델이 1개 삭제되었다

Question.objects.all()
//result: <QuerySet [<Question: 이번질문이다>]>


## Answer 생성 terminal
*** 주의할 점 ***
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.question
//이렇게 '참조하는' class가 메서드를 추가하여 제목(subject)을 표시하려는 경우 오류가 발생한다



q=Question.objects.get(id=2)
q
from django.utils import timezone
a = Answer(question=q, content='이번질문누가했니?', create_date=timezone.now())
a.save()
a.id
//result: 4

## Answer 조회 terminal
### 답변 조회
a=Answer.objects.get(id=4)
a
//result: <Answer: Answer object (4)>

### 답변에 연결된 질문 조회
a.question
//result: <Question: 이번질문이다>

### 질문을 이용하여 답변 찾기(FK 역방향)
//FK 역방향은 '연결모델명_set'으로 찾는다

q=Question.objects.get(id=2)
q.answer_set.all()
//result: <QuerySet [<Answer: Answer object (4)>]>