from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200, blank=True, null=True)
    Content=models.TextField(blank=True, null=True)
