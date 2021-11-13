from django.urls import path
from .views import *



urlpatterns = [
    path('hello',hello,name='hello'),
    path('list',movie_list,name='list'),
    path('create',create_movie,name='create'),
    path('detail/<int:pk>/',detail_movie,name='detail'),
    path('delete/<int:pk>/',delete_movie,name='delete')
]