from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('home.urls')),
    path('about', include('about.urls')), 
    path('dashboards', include('dashboards.urls')),
    path('projects', include('projects.urls')),
    path('admin', admin.site.urls),
]
