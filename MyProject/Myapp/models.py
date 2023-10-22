from django.db import models

# Create your models here.

class ProductInformation(models.Model):
    ProductId=models.CharField(max_length=122)
    ProductName=models.CharField(max_length=122)
    ProductDesc=models.TextField()
    ProductImage=models.ImageField(upload_to='Images')
    ProductPrice=models.IntegerField()
    

class UserInformation(models.Model):
    VendorName=models.CharField(max_length=122)
    VendorAddress=models.TextField()
    VendorImage=models.ImageField(upload_to="ProfileImage")
    BusinessName=models.CharField(max_length=122)
    BusinessAddress=models.TextField(max_length=122)
    GstNumber=models.CharField(max_length=122,null=True,default="No GST Number")
    BusinessLogo=models.ImageField(upload_to="Logo")
    
    