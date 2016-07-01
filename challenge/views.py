from django.shortcuts import render
from challenge.models import *

from django.http import HttpResponse, HttpResponseNotFound



# Create your views here.
def index(request):

    projects = Project.objects.all()

    return render(request, 'challenge/index-en.html', {"projects": projects})


def project(request, project_slug):

    context_dict = {}

    try:
        project = Project.objects.get(slug=project_slug)

        context_dict['project'] = project
        context_dict['team'] = Member.objects.filter(
            project=project)
        context_dict['tags'] = Tag.objects.filter(
            project=project)

    except Project.DoesNotExist:
        context_dict['project'] = {"name": "Bernardo"}

    return render(request, 'challenge/project.html', context_dict)


def department(request, department_slug):

    context_dict = {}

    try:
        department = Department.objects.get(slug=department_slug)

        context_dict['department'] = department

    except Department.DoesNotExist:
        pass

    return render(request, 'challenge/department.html', context_dict)


def member(request, member_slug):

    context_dict = {}

    try:
        member = Member.objects.get(slug=member_slug)

        context_dict['member'] = member

    except Member.DoesNotExist:
        pass

    return render(request, 'challenge/member.html', context_dict)


def sprint(request, sprint_slug):

    context_dict = {}

    try:
        sprint = Sprint.objects.get(slug=sprint_slug)

        context_dict['sprint'] = sprint

    except Sprint.DoesNotExist:
        pass

    return render(request, 'challenge/sprint.html', context_dict)

