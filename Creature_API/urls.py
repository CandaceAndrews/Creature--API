from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo', views.photo, name='photo'),
    path('add', views.add, name='add'),
]
