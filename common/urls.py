from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
    path('group/create/', views.group_create, name='group_create'),
    path('group/list/', views.group_list, name='group_list'),
    path('group/mylist/', views.group_mylist, name='group_mylist'),
    #path('group/invite/<int:group_id>/', views.group_invite, name='group_invite'),
    path('group/invite/', views.group_invite, name='group_invite'),
    # path('group/search/', search_group, name='search_group'),
    # path('group/filter/', filter_groups, name='filter_groups'),
]
