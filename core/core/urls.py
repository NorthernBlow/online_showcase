"""core URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from showcase.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('showcase.urls', namespace='showcase')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)