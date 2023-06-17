from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutpage(request):
    return render(request,'aboutpage.html',{})