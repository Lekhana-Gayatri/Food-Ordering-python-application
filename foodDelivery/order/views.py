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
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Dish, Cart, CartItem
from .serializers import CartSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request, dish_id):
    
    if request.data.get('dish_id') is not None:
        cart,created=Cart.objects.get_or_create(user=request.user)
        cart_item,created=CartItem.objects.get_or_create(cart=cart,dish_id=request.data.get('dish_id'))
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
        print(cart_item.quantity,'*'*1000)
    else:

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, id=dish_id)

        # If quantity is provided in the request data, update it
        quantity = request.data.get('quantity', 1)
        cart_item.quantity = quantity
        cart_item.save()

    return Response({"message": "Item added to cart", "quantity": cart_item.quantity}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, id=id)

    # Reduce quantity or remove item from cart
    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()

    return Response({"message": "Item removed from cart", "quantity": cart_item.quantity}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)