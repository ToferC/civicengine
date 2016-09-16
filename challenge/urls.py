from django.conf.urls import patterns, include, url
from django.contrib import admin
from challenge.views import ProjectDelete, MemberDelete, TagDelete, OrganizationDelete, RoleDelete, TeamDelete, IssueDelete, StoryDelete 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^visualize', views.visualize, name='visualize'),
    url(r'^captcha/', include('captcha.urls')),
    
    # Model urls
    url(r'^project/(?P<project_slug>[\w\-]+)/$', views.project,
        name='project'),
    url(r'^organization/(?P<organization_slug>[\w\-]+)/$', views.organization,
        name='organization'),
    url(r'^team/(?P<team_slug>[\w\-]+)/$', views.team,
        name='team'),
    url(r'^member/(?P<member_slug>[\w\-]+)/$', views.member,
        name='member'),
    url(r'^tag/(?P<tag_slug>[\w\-]+)/$', views.tag,
        name='tag'),
    url(r'^issue/(?P<issue_slug>[\w\-]+)/$', views.issue,
        name='issue'),

    # Aggregate urls
    url(r'^all_projects/$', views.all_projects, name='all_projects'),
    url(r'^all_organizations/$', views.all_organizations, name='all_organizations'),
    url(r'^all_teams/$', views.all_teams, name='all_teams'),
    url(r'^all_members/$', views.all_members, name='all_members'),
    url(r'^all_tags/$', views.all_tags, name='all_tags'),
    url(r'^all_issues/$', views.all_issues, name='all_issues'),

    # Formviews for editing
    url(r'^project_form/(?P<pk>\d+)/$', views.project_form, name='project_form'),
    url(r'^member_form/(?P<pk>\d+)/$', views.member_form, name='member_form'),
    url(r'^organization_form/(?P<pk>\d+)/$', views.organization_form, name='organization_form'),
    url(r'^team_form/(?P<pk>\d+)/$', views.team_form, name='team_form'),
    url(r'^tag_form/(?P<pk>\d+)/$', views.tag_form, name='tag_form'),
    url(r'^role_form/(?P<pk>\d+)/$', views.role_form, name='role_form'),
    url(r'^issue_form/(?P<pk>\d+)/$', views.issue_form, name='issue_form'),
    url(r'^story_form/(?P<pk>\d+)/$', views.story_form, name='story_form'),
    url(r'^response_form/(?P<pk>\d+)/$', views.response_form, name='response_form'),

    # Deleteviews
    url(r'^project_delete/(?P<pk>[0-9]+)/$', ProjectDelete.as_view(),
            name="project-delete"),
    url(r'^organization_delete/(?P<pk>[0-9]+)/$', OrganizationDelete.as_view(),
            name="organization-delete"),
    url(r'^member_delete/(?P<pk>[0-9]+)/$', MemberDelete.as_view(),
            name="member-delete"),
    url(r'^team_delete/(?P<pk>[0-9]+)/$', TeamDelete.as_view(),
            name="team-delete"),
    url(r'^tag_delete/(?P<pk>[0-9]+)/$', TagDelete.as_view(),
            name="tag-delete"),
    url(r'^role_delete/(?P<pk>[0-9]+)/$', RoleDelete.as_view(),
            name="role-delete"),
    url(r'^issue_delete/(?P<pk>[0-9]+)/$', IssueDelete.as_view(),
            name="issue-delete"),
    url(r'^story_delete/(?P<pk>[0-9]+)/$', StoryDelete.as_view(),
            name="story-delete"),

    # Add or modify views
    url(r'^add_member/$', views.add_member, name='add_member'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^add_organization/$', views.add_organization, name='add_organization'),
    url(r'^add_team/$', views.add_team, name='add_team'),
    url(r'^add_tag/$', views.add_tag, name='add_tag'),
    url(r'^add_role/(?P<team_pk>\d+)/$', views.add_role, name='add_role'),
    url(r'^apply_to_role/(?P<role_pk>\d+)/(?P<member_pk>\d+)/$', views.apply_to_role, name='apply_to_role'),
    url(r'^quit_role/(?P<role_pk>\d+)/(?P<member_pk>\d+)/$', views.quit_role, name='quit_role'),
    url(r'^add_committment/(?P<project_pk>\d+)/$', views.add_committment, name='add_committment'),
    url(r'^add_issue/$', views.add_issue, name='add_issue'),
    url(r'^add_story/(?P<issue_pk>\d+)/$', views.add_story, name='add_story'),
    url(r'^add_response/(?P<issue_pk>\d+)/$', views.add_response, name='add_response'),


    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

    #url(r'^sprint/(?P<project_slug>[\w\-]+/$)', views.sprint, name='sprint'),
    #url(r'^work/(?P<project_slug>[\w\-]+/$)', views.work, name='work'),
    url(r'^admin/', admin.site.urls),
    ]
