from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projectspage(request):
    return render(request,'projectspage.html',{})