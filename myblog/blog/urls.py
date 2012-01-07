from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'blog.views.home_views'),
    (r'^(?P<slug>[-\w]+)/$', 'blog.views.section_view'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'blog.views.detail_views'),
    (r'^(?P<year>\d{4})/$', 'blog.views.years_views'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'blog.views.months_views'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'blog.views.days_views'),
)



