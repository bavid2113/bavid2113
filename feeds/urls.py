from django.urls import path
from . import views

urlpatterns = [
    path('feeds/', views.feed_list, name='feed_list'),
]
