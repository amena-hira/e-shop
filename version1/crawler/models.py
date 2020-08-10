from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.ImageField(upload_to="pics")
class ProductInfo(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img   = models.ImageField(upload_to="pics")
    search_item  = models.CharField(max_length=255)
