from django.db import models
from django.contrib.auth.hashers import make_password,check_password
from User.models import *

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    closing_time=models.TimeField()
    rimg=models.ImageField(upload_to='dishes/',null=True,blank=True)
    def __str__(self):
        return self.name

class resAdmin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    res=models.ForeignKey(Restaurant,on_delete=models.CASCADE)

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish_name=models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True,default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    dish_img = models.ImageField(upload_to='dishes/', null=True, blank=True)
    veg = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    