
from django.urls import include, path
from django import views
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('todo',views.todolist, name='todo')
]