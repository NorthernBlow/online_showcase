from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import ListView
from .models import Category, Product, Vendor

# представление на основе классов. Репрезентация списка объектов
class VendorsViews(ListView):
    # связываем класс с моделью models.showcase.Vendor
    model = Vendor

    def head(self, *args, **kwargs):
        #context - обязательное название переменной для ListView
        context = super().get_context_data(**kwargs)
        context['title'] = timezone.now
        return context


class CategoryViews(ListView):
    model = Category



class ProductViews(ListView):
    model = Product
    context_object_name = "product"

    def head(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context