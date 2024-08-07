from django.db import models
from django.contrib.auth.models import User
from restuarant.models import *
# from django.contrib.auth.models import Group
# class orderDetails(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE,null=False)
#     dish = models.ForeignKey(Dish , on_delete=models.CASCADE,null=False)
#     to_address = models.CharField(max_length=300)
#     status = models.Choices({'cancelled':'cancelled','delivered':'delivered','pending':'pending'})
#     payment=models.BooleanField(default=False)
#
#
# class order(models.Model):
#     orderDetails=models.ForeignKey(orderDetails,on_delete=models.CASCADE,null=False)
#     deliveryPerson=models.ForeignKey()

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def add_dish(self, dish):
        cart_item, created = CartItem.objects.get_or_create(cart=self, dish=dish)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    def remove_dish(self, dish):
        cart_item = CartItem.objects.filter(cart=self, dish=dish).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"

    def get_total_price(self):
        return self.dish.price * self.quantity