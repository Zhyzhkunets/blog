from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^admin/', include(admin.site.urls)),
    #(r'^section/$', 'section_views'),
    (r'^section/(?P<name>w+)/$', 'section_views'),
    (r'^$', 'home_views'),
    (r'^post/(?P<num>\d+)/$', 'post_views'),
    (r'^(\d{4})/(?P<slug>[-w]+)/$', 'years_views'),
    (r'^(\d{4})/(\d{2})/(?P<slug>[-w]+)/$', 'months_views'),
    (r'^(\d{4})/(\d{2})/(\d{2})/(?P<slug>[-w]+)/$', 'days_views'),    
)



