# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import User,Post

from hashlib import md5



def Index(request):
    return render_to_response('index.html')

#@csrf_protect
def Login(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']
        if username=='admin' and password=='admin':
            message = 'login success'

        else:
            message = 'login failed please check username and password'

    response = {'message':message }
    
    return render_to_response('login.html' , response , context_instance=RequestContext(request) )


def Logout(request):
    message = 'successed logout'
    response = { 'message':message }
    return render_to_response('logout.html' , response )


def Archives(request):
    post = Post.objects.order_by('id')
    response = { 'post':post }
    return render_to_response('archives.html' , response )


def Usercenter(request):
     
    user = User.objects.order_by('id')
    
    return render_to_response('usercenter.html' , { 'user':user } )


def Test( request ):

    user = User.objects.order_by('name')
    
    return render_to_response('test.html' , { 'user':user } )











