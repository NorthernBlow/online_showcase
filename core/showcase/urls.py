from django.contrib import admin
from django.urls import path
from . import views



app_name = 'showcase'

urlpatterns = [
    path('', views.all_costumers, name='all_costumers'),
    path('tests/', views.test),
]