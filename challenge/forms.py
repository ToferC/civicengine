from django import forms
from django.forms import widgets
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from challenge.models import Project, Department, Member, Tag, Role

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

import datetime


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ['slug', ]
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),
        'sponsoring_departments': CheckboxSelectMultiple(),
        'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(ProjectForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, commit=True):
        instance = super(ProjectForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()
        return instance


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        exclude = ['slug', ]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(DepartmentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/department/{{ department.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, commit=True):
        instance = super(DepartmentForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()
        return instance


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        exclude = ['slug', ]
        widgets = {'tags': CheckboxSelectMultiple()}

    def __init__(self, *args, **kwargs):

        super(MemberForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/member/{{ member.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, commit=True):
        instance = super(MemberForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()
        return instance


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
        exclude = ['slug', ]

    def __init__(self, *args, **kwargs):

        super(TagForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" enctype="multipart/form-data"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))

    def save(self, commit=True):
        instance = super(TagForm, self).save(commit=False)
        instance.slug = slugify(instance.name)
        instance.save()
        return instance


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = "__all__"
        widgets = {'start_date': SelectDateWidget(),
        'end_date': SelectDateWidget(),}

    def __init__(self, *args, **kwargs):

        super(RoleForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<br><a role="button" class="btn btn-default"
                        href="/project/{{ project.slug }}">Cancel</a>"""),
                Submit('save', 'Submit'),))


