from django.contrib import admin
from challenge.models import Resource, Role, Member
from challenge.models import Organization, Project, Sprint, Work, Tag, Team
from challenge.models import Issue, Story, Vote, Response, Committment


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',
        'start_date', 
        'end_date', 
        'short_text', 
        'detail_text', 
        'submitted_date', 
        'published', )


class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'organization')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('team', 'role', 'person', 'status')


class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display= ('name', )


class SprintAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','task','duration')


class CommittmentAdmin(admin.ModelAdmin):
    list_display = ('team', 'project', 'start_date')


class IssueAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'creator', 'status', 'scope',
        'date_created', 'priority', 'rating')


class StoryAdmin(admin.ModelAdmin):
    list_display = ('name','creator', 'priority','date_created')


class VoteAdmin(admin.ModelAdmin):
    list_display = ('project','positive', 'negative', 'neutral')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('issue', 'project', 'start_date')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Committment, CommittmentAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Response, ResponseAdmin)


