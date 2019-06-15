from django.shortcuts import render
from django.http import HttpResponse
from apitest.models import Apitest,Apistep
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
  return HttpResponse("hello test") #返回 HttpResponse 响应函数

def login(request):
    return render(request, 'login.html')

#接口管理
@login_required
def apitest_manage(request):
    username = request.session.get('user','')   #读取浏览器登录session
    apitest_list = Apitest.objects.all()    #获取所有流程接口数据
    return render(request,'apitest_manage.html',{'user':username, 'apitests':apitest_list})

#接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user','')   #读取浏览器登录session
    apistep_list = Apistep.objects.all()    #获取所有接口步骤数据
    return render(request,'apistep_manage.html',{'user':username, 'apisteps':apistep_list})