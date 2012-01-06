from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'home_views'),
    (r'^(?P<slug>[-\w]+)/$', 'section_view'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'detail_views'),
    (r'^(?P<year>\d{4})/$', 'years_views'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'months_views'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'days_views'),
)



