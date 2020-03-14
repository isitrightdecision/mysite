'''
실제적인 지시가 담긴 문서
url에서 넘어와 여기서 model을 이용하여 데이터베이스와 상호작용하여 작업을 한 후,
template를 보여주게 된다.
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.")