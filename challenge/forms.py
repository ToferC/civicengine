from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from challenge.models import Project, Organization, Member, Tag
from challenge.models import Role, Team, Committment, Issue, Story, Vote, Response

from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

import datetime


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['slug', 'creator',]
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),
        'sponsoring_organizations': CheckboxSelectMultiple(),
        'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(ProjectForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Save Project'),))

    def save(self, creator, commit=True):
        instance = super(ProjectForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
        exclude = ['slug', 'creator',]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(OrganizationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/organization/{{ organization.slug }}">Cancel</a>"""),
                Submit('save', 'Save Organization'),))

    def save(self, creator, commit=True):
        instance = super(OrganizationForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        exclude = ['slug', 'creator',]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(TeamForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/team/{{ team.slug }}">Cancel</a>"""),
                Submit('save', 'Save Team'),))

    def save(self, creator, commit=True):
        instance = super(TeamForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        exclude = ['user', 'slug', ]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(MemberForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/member/{{ member.slug }}">Cancel</a>"""),
                Submit('save', 'Save Profile'),))

    def save(self, user, commit=True):
        instance = super(MemberForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.user = user
        instance.save()
        return instance


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        exclude = ['slug', 'creator',]

    def __init__(self, *args, **kwargs):

        super(TagForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/tag/{{ tag.slug }}">Cancel</a>"""),
                Submit('save', 'Save Tag'),))

    def save(self, creator, commit=True):
        instance = super(TagForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"
        exclude = ['team']
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),}

    def __init__(self, *args, **kwargs):

        super(RoleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Save Role'),))

    def save(self, team=None, commit=True):
        instance = super(RoleForm, self).save(commit=False)
        instance.team=team
        instance.save()
        return instance


class RoleApplyForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"
        exclude = ['person', 'team', 'status', 'role', 'start_date',
        'end_date', 'hrs_per_week']
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),}

    def __init__(self, *args, **kwargs):

        super(RoleApplyForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Update Position'),))

    def save(self, team=None, person=None, status=None, commit=True):
        instance = super(RoleApplyForm, self).save(commit=False)
        instance.team=team
        instance.person=person
        instance.status=status
        instance.save()
        return instance

class CommittmentForm(forms.ModelForm):
    class Meta:
        model = Committment
        fields = "__all__"
        exclude = ['project']
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),}

    def __init__(self, *args, **kwargs):

        try:
            self.user = kwargs.pop('user')
        except KeyError:
            self.user = None

        super(CommittmentForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.filter(creator=self.user)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default"
                        href="/project/{{ project.slug }}">Cancel</a> """),
                Submit('save', 'Commit Team'),))

    def save(self, project=None, commit=True):
        instance = super(CommittmentForm, self).save(commit=False)
        instance.project=project
        instance.save()
        return instance


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = "__all__"
        exclude = ['slug', 'creator', 'followers',
            'date_created', 'date_edited', 'stories',
            'rating']
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(IssueForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/issue/{{ issue.slug }}">Cancel</a>"""),
                Submit('save', 'Save Issue'),))

    def save(self, creator, commit=True):
        instance = super(IssueForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"
        exclude = ['slug', 'creator', 'followers', ''
            'date_created', 'date_edited', 'rating']
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(StoryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/issue/{{ issue.slug }}">Cancel</a>"""),
                Submit('save', 'Save Issue'),))

    def save(self, creator, issue, commit=True):
        instance = super(StoryForm, self).save(commit=False)
        instance.creator = creator
        instance.issue = issue
        instance.save()
        return instance


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = "__all__"
        exclude = ['issue']
        widgets = {'start_date': SelectDateWidget()}

    def __init__(self, *args, **kwargs):

        try:
            self.user = kwargs.pop('user')
            self.issue = kwargs.pop('issue')
        except KeyError:
            self.user = None

        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(creator=self.user)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default"
                        href="/issue/{{ issue.slug }}">Cancel</a> """),
                Submit('save', 'Link Project'),))

    def save(self, project=None, issue=None, commit=True):
        instance = super(ResponseForm, self).save(commit=False)
        instance.project=project
        instance.issue=issue
        instance.save()
        return instance


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    captcha = CaptchaField()
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'captcha')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a committment="button" class="btn btn-default"
                        href="/">Cancel</a>"""),
                Submit('save', 'Submit'),))

