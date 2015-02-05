# Create your views here.
from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import User,Article

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
    all_articles = Article.objects.order_by('id')
    
    response = { 'post':all_articles }
    return render_to_response('archives.html' , response )


def Usercenter(request):
     
    user = User.objects.filter(id=3)
    
    return render_to_response('usercenter.html' , { 'user':user } )


def SingleArticle(request , post_id):
    try:
        post_id = int(post_id)
    except ValueError:
        raise Http404()
    
    post = Article.objects.filter( article_num=post_id  )
    return render_to_response('singlearticle.html' , {'post':post} )



def Test( request ):

    post = 'sb'
    
    
    return render_to_response('test.html' , {'post':post} )











