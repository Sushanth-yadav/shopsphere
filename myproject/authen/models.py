from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProductModel(models.Model):
    pname=models.CharField(max_length=30)
    pdesc=models.CharField(max_length=30)
    price=models.IntegerField()
    pcategory=models.CharField(max_length=30)
    trending=models.BooleanField(default=False)
    offers=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)
    pimage=models.ImageField(upload_to='uploads/',default='default.png')

class CartModel(models.Model):
    pname=models.CharField(max_length=30)
    price=models.IntegerField()
    pcategory=models.CharField(max_length=30)
    quantity=models.IntegerField(default=1)
    total_price=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)