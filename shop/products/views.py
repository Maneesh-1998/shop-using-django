from django.shortcuts import render
from .models import product
# Create your views here.
from django.http import HttpResponse
def index(request):
    products=product.objects.all()
    return render(request,'index.html',{'products':products})
    #return HttpResponse("<h1> welcome to django</h1>")

def about(request):
    return HttpResponse("<h1>about page</h1>")

def contact(request):
    return HttpResponse("<h1>contact page</h1>")