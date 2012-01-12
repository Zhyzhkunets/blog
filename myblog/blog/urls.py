from django.conf.urls.defaults import *
from views import * 

urlpatterns = patterns('',
  url(r'^$', home_views),
  url(r'^(?P<slug>[-\w]+)/$', section_view),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', detail_views, name="post_url"),
  url(r'^(?P<year>\d{4})/$', years_views),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', months_views),
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', days_views),
)
