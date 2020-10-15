from django.shortcuts import render, get_object_or_404
from .models import *


def home(request):
    context = {'articles': 'haii'}
    return render(request, 'questionslist/home.html', context)
