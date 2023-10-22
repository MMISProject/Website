from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def Product(request):
    return render(request,"pages/forms/Product.html")

def AddProduct(request):
    return render(request,"pages/forms/AddProduct.html")