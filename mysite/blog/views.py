# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def Index(request):
    return render_to_response('index.html')

def Login(request):
    return render_to_response('login.html')

def Logout(request):
    return render_to_response('logout.html')

def Archives(request):
    return render_to_response('archives.html')

def Usercenter(request):
    return render_to_response('usercenter.html')

def Test(request):
    return render_to_response('test.html')