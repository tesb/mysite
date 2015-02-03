# Create your views here.
from django.http import HttpResponse 
from django.shortcuts import render_to_response
#from django.core.context_processors import csrf

from hashlib import md5



def Index(request):
    return render_to_response('index.html')


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

    return render_to_response('login.html' , response)


def Logout(request):
    message = 'successed logout'
    response = { 'message':message }
    return render_to_response('logout.html' , response )


def Archives(request,num):
    response = {'num' , num}
    return render_to_response('archives.html')


def Usercenter(request):
    baseurl = 'http://7u2m64.com1.z0.glb.clouddn.com/avatar/'
    user = {
            'username':'Jack',
            'email':'stevensin@126.com',
            'content':'I\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content testI\'m a content test',
            }
    user['avatra'] = baseurl + md5( user['email'] ).hexdigest()
    
    return render_to_response('usercenter.html', user )


def Test(request ):

    response = { 'user':
                [
                  {'username':'Jack','email':'stevensin@126.com','content':'I\'m a content'},
                  {'username':'Jack','email':'stevensin@126.com','content':'I\'m a content'},
                  {'username':'Jack','email':'stevensin@126.com','content':'I\'m a content'}
                
                ] 
                }
    resp = { 'a': [1,2,3,4,5,6,7,8,9,0,11] }
    return render_to_response('test.html' , response )











