from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^section/$', section_views),
    (r'^post/$', post_views),
    (r'^post/list_of_posts_(?P<number>\d+)/$', post_views),
    (r'^archive/(\d{4})/$', archive_years),
    (r'^archive/(\d{4})/(\d{2})/$', archive_months),
    (r'^archive/(\d{4})/(\d{2})/(\d{2})/$', achive_days),    
)



