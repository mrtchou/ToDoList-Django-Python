
from django.urls import include, path
from django import views
from . import views



urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete', views.delete_item_to_do_list, name='delete_item_to_do_list'),
    path('update_item_to_do_list/', views.update_item_to_do_list, name='update_item_to_do_list'),
]