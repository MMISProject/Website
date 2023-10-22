from django.contrib import admin
from .models import ProductInformation
# Register your models here.

@admin.register(ProductInformation)
class ProductInformation2(admin.ModelAdmin):
    list_display=['ProductId','ProductName','ProductImage','ProductPrice']

