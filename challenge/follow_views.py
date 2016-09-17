from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from challenge.models import *
from challenge.forms import *
import json

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from actstream.actions import follow, unfollow

@login_required
def follow_story(request, story_pk):

    user = request.user
    story = Story.objects.get(pk=story_pk)
