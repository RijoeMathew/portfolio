from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardspage, name="dashboardspage"),
]
