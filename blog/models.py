from django.db import models

class Section(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, max_length=500)
  
class Post(models.Model):
  title = models.CharField(max_length=50)
  slug = models.SlugField(unique=True, max_length=50)
  descrip = models.CharField(max_length=100)
  section = models.ForeignKey(Section)
  blog = models.TextField(max_length=10000)
  tags = TagField()
  creation_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(auto_now=True)
  #author =    