from rest_framework.serializers import ModelSerializer
from .models import *
class resSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields= '__all__'
class dishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields='__all__'
