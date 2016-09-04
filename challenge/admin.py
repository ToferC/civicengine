from django.contrib import admin
from challenge.models import Resource, Role, Member, Organization, Project, Sprint, Work, Tag, Team


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
    list_display = ('name',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('person', 'project', 'role')


class ResourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display= ('name', )


class SprintAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','task','duration')


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

