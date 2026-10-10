from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:name>", views.greet, name='greet'),
    path('alan', views.alan, name='alan'),
    path('ikuzwe', views.ikuzwe, name='ikuzwe')
]
