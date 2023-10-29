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
    EmailId=models.CharField(max_length=122)
    MobileNumber=models.IntegerField()
    
    
class MobileVerificationNumber(models.Model):
    MobileNumber=models.CharField(max_length=122)
    verified=models.BooleanField(default=False)
    
class SellerInformation(models.Model):
    SellerName=models.CharField(max_length=122)
    DOB=models.CharField(max_length=122)
    Primary_key=models.CharField(max_length=122)
    
class SellerBuinsessInformation(models.Model):
    BusinessName=models.CharField(max_length=122)
    GstNumber=models.CharField(max_length=122,null=True)
    Password=models.CharField(max_length=122)
    Primary_key=models.CharField(max_length=122)    

    
    
    
    