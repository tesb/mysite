from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$', 'blog.views.Index' ),
    url(r'^index/' , 'blog.views.Index'),
    url(r'^login/' , 'blog.views.Login'),
    url(r'^logout/' , 'blog.views.Logout'),
    url(r'^archives/' , 'blog.views.Archives'),
    url(r'^logout/' , 'blog.views.Logout'),
    url(r'^usercenter/' , 'blog.views.Usercenter'),

    url(r'^test/' , 'blog.views.Test'),
    
    
)


