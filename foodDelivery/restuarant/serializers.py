from rest_framework import serializers
from .models import *
class resSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields= '__all__'
class dishSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Dish
        fields=['id','dish_name','restaurant_name','rating','price','dish_img','discount','veg']
