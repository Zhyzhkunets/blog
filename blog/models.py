# encoding=utf8
from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, max_length=50)
  
class Post(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, max_length=50)
  descr = models.TextField(max_length=100)
  section = models.ForeignKey(Section)
  blog = models.TextField(max_length=100000)
  #tags = TagField()
  creation_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(null=True, blank=True)
  author = models.ForeignKey(User, null=True, blank=True, verbose_name=u"Автор")