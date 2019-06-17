from django.shortcuts import render
from django.http import HttpResponse
from apitest.models import Apitest, Apistep
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import HtmlTestRunner


# Create your views here.
def test(request):
    return HttpResponse("hello test")  # 返回 HttpResponse 响应函数


def login(request):
    return render(request, 'login.html')


# 接口管理
@login_required
def apitest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    apitest_list = Apitest.objects.all()  # 获取所有流程接口数据
    return render(request, 'apitest_manage.html', {'user': username, 'apitests': apitest_list})


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')  # 读取浏览器登录session
    apistep_list = Apistep.objects.all()  # 获取所有接口步骤数据
    return render(request, 'apistep_manage.html', {'user': username, 'apisteps': apistep_list})


# 测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()  # 统计接口数
    db = pymysql.connect(user='root', db='autotest', passwd='test123456', host='127.0.0.1')
    cursor = db.cursor()
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request, "report.html",
                  {"user": username, "apiss": apis_list, "apiscounts": apis_count, "apis_pass_counts": apis_pass_count,
                   "apis_fail_counts": apis_fail_count})  # 把值赋给apiscounts 变量
