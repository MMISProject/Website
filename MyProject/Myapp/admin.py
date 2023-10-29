from django.contrib import admin
from .models import ProductInformation,UserInformation,MobileVerificationNumber,SellerBuinsessInformation,SellerInformation
# Register your models here.

@admin.register(ProductInformation)
class ProductInformation2(admin.ModelAdmin):
    list_display=['ProductId','ProductName','ProductImage','ProductPrice']

@admin.register(UserInformation)
class UserInformation2(admin.ModelAdmin):
    list_display=['VendorImage','VendorName','BusinessName',"GstNumber"]

@admin.register(MobileVerificationNumber)
class MobileVer(admin.ModelAdmin):
    list_display=['MobileNumber','verified']
    
@admin.register(SellerInformation)
class SellerInfo(admin.ModelAdmin):
    list_display=['SellerName','DOB']
    
@admin.register(SellerBuinsessInformation)
class SellerBuinessInfo(admin.ModelAdmin):
    list_display=['BusinessName','GstNumber','Password']