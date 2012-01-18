from django.conf.urls.defaults import *
from django.views.generic import date_based
from views import *  
from myblog.blog.models import Post

years_info = {
  'queryset':Post.objects.all(),
  'date_field':'creation_date',
  'template_name ':'templates/archive_year.html',  
}

months_info = { 
  'queryset':Post.objects.all(), 
  'date_field':'creation_date',
  'template_name':'templates/archive_month.html',
}                                 

days_info = {
  'queryset':Post.objects.all(),
  'date_field':'creation_date', 
  'template_name':'templates/archive_day.html',    
  'make_object_list':True,
}                                 

urlpatterns = patterns('',
  url(r'^$', home_views),
  url(r'^(?P<slug>[-\w]+)/$', section_view),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', detail_views, name="post_url"),
  url(r'^(?P<year>\d{4})/$', date_based.archive_year, years_info, name="archive_years"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', date_based.archive_month, months_info, name="archive_months"),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', date_based.archive_day, days_info, name="archive_days"),
)  
                                