from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
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




class ProductViews(ListView):
    model = Product
    context_object_name = "product"

    def head(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    return render(request, 'showcase/home.html')


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'showcase/products/detail.html', {'product': product})


def categories(request):
    return {"categories": Category.objects.all()}


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    vendors = Vendor.objects.filter(category=category)
    return render(request, 'showcase/products/category.html', {'category': category, 'vendors': vendors})


def vendors_products():
    return {"detail": Product.objects.all()}