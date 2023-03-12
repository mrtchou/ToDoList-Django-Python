
from django.urls import include, path
from django import views
from . import views



urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete', views.delete_last_item_to_do_list, name='delete_last_item_to_do_list'),
]