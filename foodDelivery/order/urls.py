# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('save_location/', save_location, name='save_location'),
    path('add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:dish_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),

]
