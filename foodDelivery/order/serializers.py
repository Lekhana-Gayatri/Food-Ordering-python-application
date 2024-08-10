from rest_framework import serializers
from .models import CartItem

class CartSerializer(serializers.ModelSerializer):
    dish_name = serializers.CharField(source='dish.dish_name', read_only=True)
    dish_id = serializers.CharField(source='dish.id', read_only=True)
    restaurant_name = serializers.CharField(source='dish.restaurant.name', read_only=True)
    location = serializers.CharField(source='dish.restaurant.address', read_only=True)
    price = serializers.DecimalField(source='dish.price', max_digits=10, decimal_places=2, read_only=True)
    rating = serializers.FloatField(source='dish.rating', read_only=True)
    total_price=serializers.SerializerMethodField()
    class Meta:
        model = CartItem
        fields = ['id','dish_name','restaurant_name', 'price','location', 'rating', 'quantity','total_price','dish_id']
    def get_total_price(self, obj):
        return obj.get_total_price()