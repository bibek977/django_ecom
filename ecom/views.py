from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'ecom/home.html')

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def product(request):
    return HttpResponse("product")

def tracker(request):
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("search")
    
def cart(request):
    return HttpResponse("cart")