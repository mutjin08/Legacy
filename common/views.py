from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm, GroupCreationForm
from django.contrib.auth.models import User
from .models import CustomGroup as Group
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from pybo.models import Question
from django.core.paginator import Paginator


@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.leader = request.user
            group.create_date = timezone.now()
            group.save()
            group.members.add(request.user)
            group.save()
            return redirect('common:mypage')  # 마이페이지로 이동
    else:
        form = GroupCreationForm()
    return render(request, 'common/group_create.html', {'form': form})



@login_required
def group_invite(request):
    if request.method == 'POST':
        input_password = request.POST['input_password']
        group_name = request.POST['group_name']
        
        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            messages.error(request, 'Invalid group name')  # Display error message
            return render(request, 'common/group_invite.html', {'error_messages': messages.get_messages(request)})
        
        if group.password == input_password:
            group.members.add(request.user)
            return redirect('common:group_list')  # Redirect to the group list page
        else:
            messages.error(request, 'Invalid password')  # Display error message
            return render(request, 'common/group_invite.html', {'error_messages': messages.get_messages(request)})
    else:
        return render(request, 'common/group_invite.html')


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'common/group_list.html', {'groups': groups})

def group_mylist(request):
    groups = request.user.custom_groups.all()
    return render(request, 'common/group_mylist.html', {'groups': groups})

    
def mypage(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목
            Q(content__icontains=kw) |  # 내용
            Q(location__icontains=kw) |  # 장소
            Q(answer__content__icontains=kw) |  # 답변 내용
            Q(author__username__icontains=kw) |  # 질문 글쓴이
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    groups = request.user.custom_groups.all() # 내가 속한 그룹
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'groups': groups}
    return render(request, 'common/mypage.html', context)



"""def search_group(request):
    groups = CustomGroup.objects.all()
    return render(request, 'search_group.html', {'groups': groups})
    
def filter_groups(request):
    if request.method == 'GET' and request.is_ajax():
        query = request.GET.get('query')
        groups = CustomGroup.objects.filter(name__icontains=query)
        return render(request, 'group_search_list.html', {'groups': groups})"""
    
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})