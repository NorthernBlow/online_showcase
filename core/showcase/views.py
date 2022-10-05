from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    print('Hello')
    return HttpResponse('Landing')

def test(request):
    return HttpResponse('fuck')