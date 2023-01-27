from django.contrib import admin
from django.urls import path, include
from base import views



urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
]
