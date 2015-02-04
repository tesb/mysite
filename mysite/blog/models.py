from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=60)
    avatra = models.URLField()
    website = models.URLField()
    
    def __unicode__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    
    def __unicode__(self):
        return self.title + '------' + self.author


#class Publisher(models.Model):
#    name = models.CharField(max_length=30)
#    address = models.CharField(max_length=50)
#    city = models.CharField(max_length=60)
#    state_province = models.CharField(max_length=30)
#    country = models.CharField(max_length=50)
#    website = models.URLField()
#
#class Author(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=40)
#    email = models.EmailField()
#
#class Book(models.Model):
#    title = models.CharField(max_length=100)
#    authors = models.ManyToManyField(Author)
#    publisher = models.ForeignKey(Publisher)
#    publication_date = models.DateField()


