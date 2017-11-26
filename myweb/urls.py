#encoding=utf8
from django.conf.urls import include, url
from django.contrib import admin
from web01.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'myweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^read',read),
    url(r'^post/(\w+)$',body),
]
