from django.db import models

# Create your models here.
class Product(models.Model):
    idno=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()

class MyProduct(models.Model):
    idno=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()

class MyProductList(models.Model):
    idno=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
