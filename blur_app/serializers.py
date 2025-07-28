from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog, Product, Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
class ProductSerializer(serializers.ModelSerializer):
    category_title= serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model= Product
        fields= [ 'id', 'title', 'price', 'description', 'category', 'user', 'created_at','category_title']
        read_only_fields=['id', 'user', 'created_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

