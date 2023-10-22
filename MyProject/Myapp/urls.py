from . import views;
from django.urls import path

urlpatterns = [
    path('',views.index,name="Home"),
    path('Product-catogory/',views.Product,name="Product_Section"),
    path('Add-Product/',views.AddProduct,name="ProudctAdd"),
    path('Vendor-Login/',views.LogInPage,name="LoginSection")
    
]