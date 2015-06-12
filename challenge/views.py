from django.shortcuts import render
from challenge.models import *

# Create your views here.
def index(request):
    return render(request, 'challenge/index-en.html', {})
