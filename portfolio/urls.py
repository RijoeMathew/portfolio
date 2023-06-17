from django.contrib import admin
from django.urls import path,include
from home import urls
from about import urls
from dashboards import urls

urlpatterns = [
    path('', include('home.urls')),
    path('about', include('about.urls')), 
    path('dashboards', include('dashboards.urls')),
    path('admin', admin.site.urls),
]
