from django.conf.urls.defaults import *
from django.views.generic import list_detail
from views import *  

years_info = {
  'queryset':Post.object.all(),
  'date_field':'creation_date', 
  'template_name ':'templates/archive_years.html', 
  'make_object_list'=True, 
}

 months_info = { 
  'queryset':Post.object.all(), 
  'date_field':'creation_date',   
  'template_name':'templates/archive_months.html',   
}                                 

posts_info = {
  'queryset':Post.object.all(),
  'date_field':'creation_date',  
  'template_name':'templates/archive_days.html',    
                    }                                 
#detail_views = {}                                 

urlpatterns = patterns('',
  url(r'^$', home_views),
  url(r'^(?P<slug>[-\w]+)/$', section_view),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', detail_views, name="post_url"),
)  
                          
urlpatterns +=patterns('django.views.generic.date_based' 
  url(r'^(?P<year>\d{4})/$','archive_month', month_info),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_day', day_info),  
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'object_detail', posts_info),
                                