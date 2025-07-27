from django.db import models

# Create your models here.

class Student(models.Model):
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200, blank=True, null=True)
    age=models.CharField(max_length=200,default=1)

class Employee(models.Model):
    fullname=models.CharField(max_length=200)
    salary=models.DecimalField(decimal_places=4, max_digits=10)
    address=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    age=models.CharField(max_length=200)



