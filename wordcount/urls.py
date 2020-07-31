
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('hola/',views.hola),
    path('wordcount/', views.count, name='countpage'),
    path('about/', views.about, name = 'about')
]
