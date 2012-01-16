from django.shortcuts import render_to_response
from models import *
import datetime
from django.views.generic import date_based, list_detail

def home_views(request):
  posts = Post.objects.all()#.order_by('-published_date')
  return render_to_response('home.html', {'posts':posts})
  
def section_view(request, slug):
  #section = Section.objects.get(slug=slug)
  #posts = Post.objects.filter(section=section)
  posts = Post.objects.filter(section=Section.objects.get(slug=slug))#.order_by('-published_date')
  return render_to_response('section_view.html', {'posts':posts})   

def detail_views(request, year, month, day, slug):
  post = Post.objects.get(creation_date__year=year, creation_date__month=month, creation_date__day=day, slug=slug)
  return render_to_response('detail_views.html', {'post':post})

#def years_views(request, year):
#  posts = Post.objects.filter(creation_date__year=year)#.order_by('-published_date')
#  return render_to_response('years_views.html', {'posts':posts})

#def months_views(request, year, month):
#  posts = Post.objects.filter(creation_date__year=year, creation_date__month=month)#.order_by('-published_date')
#  return render_to_response('months_views.html', {'posts':posts})

#def day_views(request, year, month, day):
#  posts = Post.objects.filter(creation_date__year=year, creation_date__month=month, creation_date__day=day)#.order_by('-published_date')
#  return render_to_response('days_views.html', {'posts':posts})

    
