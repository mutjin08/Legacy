# 로그인과 로그아웃
python manage.py runserver 0:80




#로그인
## 환경 구현
### /workspace/mysite/config/settings.py
INSTALLED_APPS <- 'django.contrib.auth' 추가





## common 앱 생성
로그인·로그아웃을 pybo와 분리시켜 구현한다

### terminal
django-admin startapp common

### /workspace/mysite/config/settings.py
INSTALLED_APPS <- 'common.apps.CommonConfig' 추가

### /workspace/mysite/config/urls.py
URL_PATTERNS <- path('common/', include('common.urls')) 추가

# 로그인 기능 구현
### /workspace/mysite/templates/navbar.html
<a href="{% url 'common:login' %}">login</a> 추가

### mysite/common/urls.py
URL 매핑 규칙을 추가

LoginView는 /mysite/template/registeration/login.html 찾는다
-> /mysite/template/common/login.html 에서 찾도록 변경한다

path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
하지만 아직 /mysite/template/registeration/login.html이 없으므로 생성해야 한다




## 로그인 템플릿
### /workspace/mysite/templates/common
common(로그인)관련 template들이 들어갈 dir 생성

### /workspace/mysite/templates/common/login.html
로그인 직후 리다이렉트되는 login.html 을 작성한다.
사용자 id와 pw를 입력으로 받아 로그인한다.


### /workspace/mysite/templates/form_errors.html
로그인 실패시 왜 로그인이 실패했는지 알려주는 역할을 한다.

# 로그인 수행
이전에 생성했던 superuser로 로그인하면 로그인은 성공하나 404 error 발생
오류가 발생한 이유: django.contrib.auth 패키지는 디폴트로 /accounts/profile/ 이라는 URL 로 이동시키기 때문이다.
이 프로젝트의 url 구조와 맞지 않으므로 로그인 성공 시 / 페이지로 이동할 수 있게 해야 한다.



## 로그인 성공 후 이동하는 url 변경
### /workspace/mysite/config/settings.py
LOGIN_REDIRECT_URL = '/' 삽입

/에 대한 url 매핑 규칙을 작성하지 않았으므로 여전히 error가 발생한다.
## /에 대한 url 매핑 규칙을 작성
### mysite/config/urls.py