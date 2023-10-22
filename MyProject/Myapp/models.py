from django.db import models

# Create your models here.

class ProductInformation(models.Model):
    ProductId=models.CharField(max_length=122)
    ProductName=models.CharField(max_length=122)
    ProductImage=models.ImageField(upload_to='Images')
    ProductPrice=models.IntegerField()
    