"""studygroupsite URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')), # include the view of the base sub-app
]

