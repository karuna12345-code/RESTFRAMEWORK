from rest_framework import serializers
from .models import Blog, Product, Category
from django.contrib.auth import get_user_model

User=get_user_model()
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
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model= Category
        fields= ['id','title','created_at','product']



