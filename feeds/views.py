from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def feed_list(request):
    return HttpResponse("This is the feed list page.")

