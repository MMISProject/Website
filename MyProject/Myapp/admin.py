from django.contrib import admin
from .models import ProductInformation,UserInformation
# Register your models here.

@admin.register(ProductInformation)
class ProductInformation2(admin.ModelAdmin):
    list_display=['ProductId','ProductName','ProductImage','ProductPrice']

@admin.register(UserInformation)
class UserInformation2(admin.ModelAdmin):
    list_display=['BusinessLogo','VendorName','BusinessName',"GstNumber"]
