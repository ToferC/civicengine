from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^visualize', views.visualize, name='visualize'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^project/(?P<project_slug>[\w\-]+)/$', views.project,
        name='project'),
    url(r'^department/(?P<department_slug>[\w\-]+)/$', views.department,
        name='department'),
    url(r'^lab/(?P<lab_slug>[\w\-]+)/$', views.lab,
        name='lab'),
    url(r'^member/(?P<member_slug>[\w\-]+)/$', views.member,
        name='member'),
    url(r'^tag/(?P<tag_slug>[\w\-]+)/$', views.tag,
        name='tag'),

    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^all_departments/$', views.all_departments, name='all_departments'),
    url(r'^all_labs/$', views.all_labs, name='all_labs'),
    url(r'^all_members/$', views.all_members, name='all_members'),
    url(r'^all_tags/$', views.all_tags, name='all_tags'),

    url(r'^add_member/$', views.add_member, name='add_member'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^add_department/$', views.add_department, name='add_department'),
    url(r'^add_lab/$', views.add_lab, name='add_lab'),
    url(r'^add_tag/$', views.add_tag, name='add_tag'),
    url(r'^add_role/$', views.add_role, name='add_role'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #url(r'^sprint/(?P<project_slug>[\w\-]+/$)', views.sprint, name='sprint'),
    #url(r'^work/(?P<project_slug>[\w\-]+/$)', views.work, name='work'),
    url(r'^admin/', admin.site.urls),
    ]
