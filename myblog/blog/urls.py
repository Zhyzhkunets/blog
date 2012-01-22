from django.conf.urls.defaults import *
from django.views.generic import date_based, list_detail
from myblog.blog.models import Post
from time import strftime
from views import *  
import time

home_info = {
  'queryset':Post.objects.all(),
  'template_name':'home.html',
}

years_info = {
  'queryset':Post.objects.all(),
  'date_field':'creation_date',
  'template_name':'archive_year.html',  
}

months_info = { 
  'queryset':Post.objects.all(), 
  'date_field':'creation_date',
  'template_name':'archive_month.html',
  'month_format':time.strftime('%m'),
}                                 

days_info = {
  'queryset':Post.objects.all(),
  'date_field':'creation_date', 
  'template_name':'archive_day.html',    
  'month_format':time.strftime('%m'),
}                                 

detail_info = {
  'queryset':Post.objects.all(),
  'date_field':'creation_date',
  'slug_field':'slug',
  'month_format':time.strftime('%m'),
  'template_name':'detail_views.html',
  'template_object_name':'item',
  'extra_context':{'post':Post.objects.all()},
}

urlpatterns = patterns('',
  url(r'^$', list_detail.object_list, home_info),
  url(r'^(?P<year>\d{4})/$', date_based.archive_year, years_info, name="archive_years"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', date_based.archive_month, months_info, name="archive_months"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', date_based.archive_day, days_info, name="archive_days"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', date_based.object_detail, detail_info, name="post_url"),      
  #url(r'^(?P<slug>[-\w]+)/$', section_view),
)  
                                