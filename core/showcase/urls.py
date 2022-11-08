from django.contrib import admin
from django.urls import path
from . import views



app_name = 'showcase'

urlpatterns = [
    path('', views.index, name='index'),
    path('vendors/', views.VendorsViews.as_view(template_name="vendor_list.html")),
    path('products/', views.ProductViews.as_view()),
    #path('tests/', views.test),
]