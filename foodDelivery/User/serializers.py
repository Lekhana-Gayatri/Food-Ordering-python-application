from rest_framework.serializers import ModelSerializer
from .models import *
class userSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
