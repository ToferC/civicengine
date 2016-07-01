from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^project/(?P<project_slug>[\w\-]+)/$', views.project,
        name='project'),
    url(r'^department/(?P<project_slug>[\w\-]+)/$', views.department,
        name='department'),
    url(r'^member/(?P<project_slug>[\w\-]+)/$', views.member,
        name='member'),
    #url(r'^sprint/(?P<project_slug>[\w\-]+/$)', views.sprint, name='sprint'),
    #url(r'^work/(?P<project_slug>[\w\-]+/$)', views.work, name='work'),
    url(r'^admin/', admin.site.urls),
    ]
