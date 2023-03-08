
from django.urls import include, path


urlpatterns = [
    path('', include('to_do_list.urls')),
]


