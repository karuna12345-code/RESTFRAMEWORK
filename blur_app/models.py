from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200, blank=True, null=True)
    Content=models.TextField(blank=True, null=True)


class Category(models.Model):
    title=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Product(models.Model):
    title= models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(blank=True, null= True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    


