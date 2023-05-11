from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕 나는 수진이야")