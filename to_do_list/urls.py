
from django.urls import include, path
from django import views
from . import views



urlpatterns = [
    path('', views.todolist, name='todolist'),
]