from django.shortcuts import render_to_response
from mysite.blog.models import Post, Section

def home_views(request):
  posts = Post.objects.order_by('-id')
  sections = Section.objects.order_by('-id')
  return render_to_response('post.html', {'posts':pots, 'sections':sections})
  
def section_views(request, name):
  posts = Post.objects.filter(section=name).order_by('-id')
  sections = Section.objects.order_by('-id')
  return render_to_response('post.html', {'posts':pots, 'sections':sections})
               
def post_views(request, num="1"):
  posts = Post.objects.filter(id=num)
  sections = Section.objects.order_by('-id')
  return render_to_response('post.html', {'posts':pots, 'sections':sections})
