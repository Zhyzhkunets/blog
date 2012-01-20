from django.conf.urls.defaults import *
from django.views.generic import date_based
from myblog.blog.models import Post
from time import strftime
from views import *  
import time


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

urlpatterns = patterns('',
  url(r'^$', home_views),
  url(r'^(?P<year>\d{4})/$', date_based.archive_year, years_info, name="archive_years"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', date_based.archive_month, months_info, name="archive_months"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', date_based.archive_day, days_info, name="archive_days"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', detail_views, name="post_url"),      
  #url(r'^(?P<slug>[-\w]+)/$', section_view),
)  
                                