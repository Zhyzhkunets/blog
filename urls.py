from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    #(r'^section/$', section_views),
    #(r'^section/(?P<name>w+)/$', section_views),
    #(r'^post/$', post_views),
    #(r'^post/(?P<number>\d+)/$', post_views),
    #(r'^archive/(\d{4})/$', years_views),
    #(r'^archive/(\d{4})/(\d{2})/$', months_views),
    #(r'^archive/(\d{4})/(\d{2})/(\d{2})/$', days_views),    
)



