from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from challenge.models import *
from challenge.forms import *
import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



# Create your views here.
def index(request):

    context_dict = {}

    projects = Project.objects.all()
    departments = Department.objects.all()
    members = Member.objects.all()
    tags = Tag.objects.all()

    context_dict['projects'] = projects
    context_dict['departments'] = departments
    context_dict['members'] = members
    context_dict['tags'] = tags

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


def all_departments(request):
    context_dict = {}

    departments = Department.objects.all()

    context_dict['departments'] = departments

    return render(request, 'challenge/all_departments.html', context_dict)


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
        context_dict['sponsoring_departments'] = Department.objects.filter(
            project=project)
        context_dict['project'] = project
        context_dict['tags'] = Tag.objects.filter(
            project=project)

        team = Role.objects.filter(project=project)

        context_dict['team'] = team

    except Project.DoesNotExist:
        context_dict['project'] = {"name": "Bernardo"}

    return render(request, 'challenge/project.html', context_dict)


def department(request, department_slug):

    context_dict = {}

    try:
        department = Department.objects.get(slug=department_slug)

        context_dict['department'] = department
        context_dict['tags'] = Tag.objects.filter(
            department=department)
        context_dict['projects'] = Project.objects.filter(
            sponsoring_departments=department)
        context_dict['members'] = Member.objects.filter(
            department=department)
        context_dict['image'] = department.image

    except Department.DoesNotExist:
        pass

    return render(request, 'challenge/department.html', context_dict)


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
        context_dict['departments'] = Department.objects.filter(
            tags=tag)
        context_dict['projects'] = Project.objects.filter(
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

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            slug = slugify(project_form.cleaned_data['name'])

            project_form.save(commit=True)

            return HttpResponseRedirect("/project/{}".format(slug))

        else:
            print (project_form.errors)

    else:

        project_form = ProjectForm()

    return render(request, 'challenge/add_project.html',
        {'project_form': project_form})

@login_required
def add_department(request):

    if request.method == 'POST':
        department_form = DepartmentForm(request.POST, request.FILES)

        if department_form.is_valid():
            slug = slugify(department_form.cleaned_data['name'])

            department_form.save(commit=True)

            return HttpResponseRedirect("/department/{}".format(slug))

        else:
            print (department_form.errors)

    else:

        department_form = DepartmentForm()

    return render(request, 'challenge/add_department.html',
        {'department_form': department_form})

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

    if request.method == 'POST':
        tag_form = TagForm(request.POST, request.FILES)

        if tag_form.is_valid():
            slug = slugify(tag_form.cleaned_data['name'])

            tag_form.save(commit=True)

            return HttpResponseRedirect("/tag/{}".format(slug))

        else:
            print (tag_form.errors)

    else:

        tag_form = TagForm()

    return render(request, 'challenge/add_tag.html',
        {'tag_form': tag_form})

@login_required
def add_role(request):

    if request.method == 'POST':
        role_form = RoleForm(request.POST, request.FILES)

        if role_form.is_valid():
            slug = slugify("{}-{}".format(role_form.cleaned_data['project'],
                role_form.cleaned_data['person']))

            role_form.save(commit=True)

            return HttpResponseRedirect("/project/{}".format(slugify(
                role_form.cleaned_data['project'])))

        else:
            print (role_form.errors)

    else:

        role_form = RoleForm()

    return render(request, 'challenge/add_role.html',
        {'role_form': role_form})


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
