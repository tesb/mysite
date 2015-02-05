from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=20 )
    email = models.EmailField( max_length=75 , verbose_name='e-mail' )
    address = models.CharField(max_length=60)
    avatra = models.URLField()
    reg_ip = models.IPAddressField(default='0.0.0.0')
    website = models.URLField()
    
    def __unicode__(self):
        return u'%s' % (self.name)

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateField( auto_now = False, auto_now_add = False  )
    article_num = models.CharField(max_length=50 , unique=True)
    
    def __unicode__(self):
        return u'%s ' % ( self.title )


class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    pubdate = models.DateTimeField( 'date published' )

    def __unicode__(self):
        return self.question


