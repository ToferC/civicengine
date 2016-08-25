from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from challenge.models import Project, Organization, Member, Tag, Role, Lab

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
                HTML("""<br><a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Create Project'),))

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
                HTML("""<br><a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/organization/{{ organization.slug }}">Cancel</a>"""),
                Submit('save', 'Create Organization'),))

    def save(self, creator, commit=True):
        instance = super(OrganizationForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.creator = creator
        instance.save()
        return instance


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = "__all__"
        exclude = ['slug', 'creator',]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(LabForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/lab/{{ lab.slug }}">Cancel</a>"""),
                Submit('save', 'Create Lab'),))

    def save(self, creator, commit=True):
        instance = super(LabForm, self).save(commit=False)
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
                HTML("""<br><a role="button" class="btn btn-default" enctype="multipart/form-data"
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
                HTML("""<br><a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/tag/{{ tag.slug }}">Cancel</a>"""),
                Submit('save', 'Create Tag'),))

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
        exclude = ['person',]
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),}

    def __init__(self, *args, **kwargs):

        super(RoleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a role="button" class="btn btn-default"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Join Project'),))

    def save(self, person=None, commit=True):
        instance = super(RoleForm, self).save(commit=False)
        instance.person=person
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
                HTML("""<br><a role="button" class="btn btn-default"
                        href="/">Cancel</a>"""),
                Submit('save', 'Submit'),))

