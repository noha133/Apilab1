from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter



urlpatterns = [

    path('hello',hello,name='hello'),
    path('signup',sign_up,name='signup'),
    path('login', obtain_auth_token, name="login"),
    path('logout', log_out, name="logout"),
    path('list',movie_list,name='list'),
    path('create',create_movie,name='create'),
    path('detail/<int:pk>/',detail_movie,name='detail'),
    path('delete/<int:pk>/',delete_movie,name='delete')
]