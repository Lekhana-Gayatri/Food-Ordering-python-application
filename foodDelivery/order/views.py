from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def save_location(request):
    if request.method == 'POST':
        print('*'*100)
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(latitude,longitude)
        return JsonResponse({'message': 'Location saved successfully.'})

    return render(request,"gps.html")

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Dish, Cart, CartItem

@login_required
def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.add_dish(dish)
    return redirect('cart_detail')

@login_required
def remove_from_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart.remove_dish(dish)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})
