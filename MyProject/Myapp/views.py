from django.shortcuts import render
from .models import ProductInformation
# Create your views here.

def index(request):
    return render(request,"index.html")

def Product(request):
    return render(request,"pages/forms/Product.html")

def AddProduct(request):
    
    if request.method=="POST":
        pName=request.POST['productName']
        pPrice=request.POST['productPrice']
        pDescription=request.POST['productDescription']
        pImage=request.POST['images']
        pInformation=ProductInformation()
    return render(request,"pages/forms/AddProduct.html")


def LogInPage(request):
    return render(request,"pages/samples/login.html")
