from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomGroup as Group


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class GroupCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Group
        fields = ['name', 'password', 'introduction']
        labels = {
            'name' : '그룹이름',
            'password' : '그룹비밀번호',
            'introduction' : '그룹소개',
        }