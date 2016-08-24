from django.conf.urls import patterns, include, url
from django.contrib import admin
from challenge.views import ProjectUpdate, MemberUpdate, TagUpdate, OrganizationUpdate, LabUpdate, RoleUpdate
from challenge.views import ProjectDelete, MemberDelete, TagDelete, OrganizationDelete, RoleDelete, LabDelete 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^visualize', views.visualize, name='visualize'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^project/(?P<project_slug>[\w\-]+)/$', views.project,
        name='project'),
    url(r'^organization/(?P<organization_slug>[\w\-]+)/$', views.organization,
        name='organization'),
    url(r'^lab/(?P<lab_slug>[\w\-]+)/$', views.lab,
        name='lab'),
    url(r'^member/(?P<member_slug>[\w\-]+)/$', views.member,
        name='member'),
    url(r'^tag/(?P<tag_slug>[\w\-]+)/$', views.tag,
        name='tag'),

    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^all_organizations/$', views.all_organizations, name='all_organizations'),
    url(r'^all_labs/$', views.all_labs, name='all_labs'),
    url(r'^all_members/$', views.all_members, name='all_members'),
    url(r'^all_tags/$', views.all_tags, name='all_tags'),

    # Formviews for editing
    url(r'^project_form/(?P<pk>[0-9]+)/$', ProjectUpdate.as_view(), name='project-update'),
    url(r'^member_form/(?P<pk>[0-9]+)/$', MemberUpdate.as_view(), name='member-update'),
    url(r'^organization_form/(?P<pk>[0-9]+)/$', OrganizationUpdate.as_view(), name='organization-update'),
    url(r'^lab_form/(?P<pk>[0-9]+)/$', LabUpdate.as_view(), name='lab-update'),
    url(r'^tag_form/(?P<pk>[0-9]+)/$', TagUpdate.as_view(), name='tag-update'),
    url(r'^role_form/(?P<pk>[0-9]+)/$', RoleUpdate.as_view(), name='role-update'),

    # Deleteviews
    url(r'^project_delete/(?P<pk>[0-9]+)/$', ProjectDelete.as_view(),
            name="project-delete"),
    url(r'^organization_delete/(?P<pk>[0-9]+)/$', OrganizationDelete.as_view(),
            name="organization-delete"),
    url(r'^member_delete/(?P<pk>[0-9]+)/$', MemberDelete.as_view(),
            name="member-delete"),
    url(r'^lab_delete/(?P<pk>[0-9]+)/$', LabDelete.as_view(),
            name="lab-delete"),
    url(r'^tag_delete/(?P<pk>[0-9]+)/$', TagDelete.as_view(),
            name="tag-delete"),
    url(r'^role_delete/(?P<pk>[0-9]+)/$', RoleDelete.as_view(),
            name="role-delete"),

    url(r'^add_member/$', views.add_member, name='add_member'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^add_organization/$', views.add_organization, name='add_organization'),
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
