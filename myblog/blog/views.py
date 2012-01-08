from django.shortcuts import render_to_response
from models import *

def home_views(request):
  posts = Post.objects.all().order_by('-id')
  return render_to_response('home.html', {'posts':posts})
  
def section_view(request, slug='section'):
  sections = Section.objects.all()
  return render_to_response('section_view.html', {'sections':section})   

def detail_views(request, year, month, day, slug):
  return render_to_response('detail_views.html', {'detail':'this is detail page'})

def years_views(request, year):
  return render_to_response('years_views.html', {'years':'this is years page'})

def months_views(request, year, month):
  return render_to_response('months_views.html', {'months':'this is months page'})

def days_views(request, year, month, day):
  return render_to_response('days_views.html', {'days':'this is days page'})
   
