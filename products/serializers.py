from rest_framework import serializers
from .models import Product, Category, ProductReview


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'image']


class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = ProductReview
        fields = ['id', 'user', 'rating', 'comment', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    reviews = ProductReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'category',
            'coffee_type', 'roast_level', 'origin', 'weight',
            'price', 'available', 'stock', 'image', 'reviews',
            'created_at', 'updated_at'
        ]