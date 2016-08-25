from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from challenge.models import *
from challenge.forms import *
import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



# Basic Views

def index(request):

    context_dict = {}

    projects = Project.objects.all()
    organizations = Organization.objects.all()
    members = Member.objects.all()
    tags = Tag.objects.all()
    labs = Lab.objects.all()

    context_dict['projects'] = projects
    context_dict['organizations'] = organizations
    context_dict['members'] = members
    context_dict['tags'] = tags
    context_dict['labs'] = labs

    return render(request, 'challenge/index-en.html', context_dict)


def visualize(request):

    context_dict = {}

    with open('flare.py') as data_file:
        data = json.load(data_file)

    context_dict['data'] = data

    return render(request, 'challenge/visualize.html', context_dict)


def all_projects(request):
    context_dict = {}

    projects = Project.objects.all()

    context_dict['projects'] = projects

    return render(request, 'challenge/all_projects.html', context_dict)


def all_organizations(request):
    context_dict = {}

    organizations = Organization.objects.all()

    context_dict['organizations'] = organizations

    return render(request, 'challenge/all_organizations.html', context_dict)


def all_labs(request):
    context_dict = {}

    labs = Lab.objects.all()

    context_dict['labs'] = labs

    return render(request, 'challenge/all_labs.html', context_dict)


def all_members(request):
    context_dict = {}

    members = Member.objects.all()

    context_dict['members'] = members

    return render(request, 'challenge/all_members.html', context_dict)


def all_tags(request):
    context_dict = {}

    tags = Tag.objects.all()

    context_dict['tags'] = tags

    return render(request, 'challenge/all_tags.html', context_dict)


def project(request, project_slug):

    context_dict = {}

    try:
        project = Project.objects.get(slug=project_slug)
        context_dict['sponsoring_organizations'] = Organization.objects.filter(
            project=project)
        context_dict['labs'] = Lab.objects.filter(
            project=project)
        context_dict['project'] = project
        context_dict['tags'] = Tag.objects.filter(
            project=project)

        team = Role.objects.filter(project=project)

        context_dict['team'] = team

    except Project.DoesNotExist:
        context_dict['project'] = {"name": "Bernardo"}

    return render(request, 'challenge/project.html', context_dict)


def organization(request, organization_slug):

    context_dict = {}

    try:
        organization = Organization.objects.get(slug=organization_slug)

        context_dict['organization'] = organization
        context_dict['tags'] = Tag.objects.filter(
            organization=organization)
        context_dict['projects'] = Project.objects.filter(
            sponsoring_organizations=organization)
        context_dict['members'] = Member.objects.filter(
            organization=organization)
        context_dict['image'] = organization.image

    except Organization.DoesNotExist:
        pass

    return render(request, 'challenge/organization.html', context_dict)


def lab(request, lab_slug):

    context_dict = {}

    try:
        lab = Lab.objects.get(slug=lab_slug)

        context_dict['lab'] = lab
        context_dict['tags'] = Tag.objects.filter(
            lab=lab)
        context_dict['projects'] = Project.objects.filter(
            labs=lab)
        context_dict['members'] = Member.objects.filter(
            lab=lab)
        context_dict['image'] = lab.image

    except Lab.DoesNotExist:
        pass

    return render(request, 'challenge/lab.html', context_dict)


def member(request, member_slug):

    context_dict = {}

    try:
        member = Member.objects.get(slug=member_slug)

        context_dict['member'] = member
        context_dict['tags'] = Tag.objects.filter(
            member=member)
        context_dict['projects'] = Role.objects.filter(
            person=member)

    except Member.DoesNotExist:
        pass

    return render(request, 'challenge/member.html', context_dict)


def tag(request, tag_slug):

    context_dict = {}

    try:
        tag = Tag.objects.get(slug=tag_slug)

        context_dict['tag'] = tag
        context_dict['members'] = Member.objects.filter(
            tags=tag)
        context_dict['organizations'] = Organization.objects.filter(
            tags=tag)
        context_dict['projects'] = Project.objects.filter(
            tags=tag)
        context_dict['labs'] = Lab.objects.filter(
            tags=tag)

    except Member.DoesNotExist:
        pass

    return render(request, 'challenge/tag.html', context_dict)


def sprint(request, sprint_slug):

    context_dict = {}

    try:
        sprint = Sprint.objects.get(slug=sprint_slug)

        context_dict['sprint'] = sprint

    except Sprint.DoesNotExist:
        pass

    return render(request, 'challenge/sprint.html', context_dict)


def work(request, work_slug):

    context_dict = {}

    try:
        sprint = Work.objects.get(slug=work_slug)

        context_dict['work'] = work

    except Work.DoesNotExist:
        pass

    return render(request, 'challenge/work.html', context_dict)


# Add content views
@login_required
def add_project(request):

    user = request.user

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            slug = slugify(project_form.cleaned_data['name'])

            project_form.save(creator=user, commit=True)

            return HttpResponseRedirect("/project/{}".format(slug))

        else:
            print (project_form.errors)

    else:

        project_form = ProjectForm()

    return render(request, 'challenge/add_project.html',
        {'project_form': project_form})


@login_required
def add_organization(request):

    user = request.user

    if request.method == 'POST':
        organization_form = OrganizationForm(request.POST, request.FILES)

        if organization_form.is_valid():
            slug = slugify(organization_form.cleaned_data['name'])

            organization_form.save(creator=user, commit=True)

            return HttpResponseRedirect("/organization/{}".format(slug))

        else:
            print (organization_form.errors)

    else:

        organization_form = OrganizationForm()

    return render(request, 'challenge/add_organization.html',
        {'organization_form': organization_form})


@login_required
def add_lab(request):

    user = request.user

    if request.method == 'POST':
        lab_form = LabForm(request.POST, request.FILES)

        if lab_form.is_valid():
            slug = slugify(lab_form.cleaned_data['name'])

            lab_form.save(creator=user, commit=True)

            return HttpResponseRedirect("/lab/{}".format(slug))

        else:
            print (lab_form.errors)

    else:

        lab_form = LabForm()

    return render(request, 'challenge/add_lab.html',
        {'lab_form': lab_form})


@login_required
def add_member(request):

    user = request.user

    if request.method == 'POST':
        member_form = MemberForm(request.POST, request.FILES)

        if member_form.is_valid():
            slug = slugify(member_form.cleaned_data['name'])

            member_form.save(user=user, commit=True)

            return HttpResponseRedirect("/member/{}".format(slug))

        else:
            print (member_form.errors)

    else:

        member_form = MemberForm()

    return render(request, 'challenge/add_member.html',
        {'member_form': member_form})


@login_required
def add_tag(request):

    user = request.user

    if request.method == 'POST':
        tag_form = TagForm(request.POST, request.FILES)

        if tag_form.is_valid():
            slug = slugify(tag_form.cleaned_data['name'])

            tag_form.save(creator=user, commit=True)

            return HttpResponseRedirect("/tag/{}".format(slug))

        else:
            print (tag_form.errors)

    else:

        tag_form = TagForm()

    return render(request, 'challenge/add_tag.html',
        {'tag_form': tag_form})


@login_required
def add_role(request):

    user = request.user
    member = Member.objects.get(user=user)

    if request.method == 'POST':
        role_form = RoleForm(request.POST, request.FILES)

        if role_form.is_valid():

            role_form.save(person=member, commit=True)

            return HttpResponseRedirect("/project/{}".format(slugify(
                role_form.cleaned_data['project'])))

        else:
            print (role_form.errors)

    else:

        role_form = RoleForm()

    return render(request, 'challenge/add_role.html',
        {'role_form': role_form})


# Update & Delete Views

class ProjectUpdate(UpdateView):
    model = Project
    fields = "__all__"
    exclude = ['slug', 'creator',]

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(ProjectUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdate,
            self).dispatch(*args, **kwargs)


class ProjectDelete(DeleteView):
    model = Project


class OrganizationUpdate(UpdateView):
    model = Organization
    fields = "__all__"
    exclude = ['slug', 'creator',]

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(OrganizationUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrganizationUpdate,
            self).dispatch(*args, **kwargs)


class OrganizationDelete(DeleteView):
    model = Organization


class MemberUpdate(UpdateView):
    model = Member
    fields = "__all__"
    exclude = ['slLab',]

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(MemberUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MemberUpdate,
            self).dispatch(*args, **kwargs)


class MemberDelete(DeleteView):
    model = Member


class LabUpdate(UpdateView):
    model = Lab
    fields = "__all__"
    exclude = ['slug', 'creator',]

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(LabUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LabUpdate,
            self).dispatch(*args, **kwargs)


class LabDelete(DeleteView):
    model = Lab


class TagUpdate(UpdateView):
    model = Tag
    fields = "__all__"
    exclude = ['slug', 'creator',]

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super(TagUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TagUpdate,
            self).dispatch(*args, **kwargs)


class TagDelete(DeleteView):
    model = Tag


class RoleUpdate(UpdateView):
    model = Role
    fields = "__all__"

    def form_valid(self, form):

        return super(RoleUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RoleUpdate,
            self).dispatch(*args, **kwargs)


class RoleDelete(DeleteView):
    model = Role


# Admin Views

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
            messages.info(request, "Thanks for registering. You are now logged in.")


            if user.is_active:

                user = authenticate(
                    username=user_form.cleaned_data['username'],
                    password=user_form.cleaned_data['password'],
                                    )
                login(request, user)

                return HttpResponseRedirect('/add_member/')

            else:
                print("Invalid login details: {}, {}".format(username, password))
                return HttpResponse("Invalid login details supplied.")

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'challenge/register.html',
        {'user_form': user_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")

        else:
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'challenge/login.html', {})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/')
