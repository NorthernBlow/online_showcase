from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.
def all_costumers(request):
    products = Product.objects.all()
    print(request)
    print('Hello')
    return render(request, 'showcase/home.html', {'costumers': products})

def test(request):
    return HttpResponse('fuck')