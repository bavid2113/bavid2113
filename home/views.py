from django.shortcuts import render

# Create your views here.
# home/views.py

from django.http import HttpResponse

def feed_list(request):
    return HttpResponse("Welcome to the Home Page!")
