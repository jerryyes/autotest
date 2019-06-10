from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
  return HttpResponse("hello test") #返回 HttpResponse 响应函数
