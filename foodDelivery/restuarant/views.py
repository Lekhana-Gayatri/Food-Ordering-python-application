from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .permissions import *
from rest_framework import status
from django.http import response
from django.db.models import Q
from django.http import JsonResponse
class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        if query:
            dishes = Dish.objects.filter(Q(dish_name__icontains=query))
        else:
            dishes = Dish.objects.all()
        dishes_data = [{"id": dish.id, "dish_name": dish.dish_name, "price": dish.price, "description": dish.description, "dish_img": dish.dish_img.url if dish.dish_img else None, "rating": dish.rating} for dish in dishes]
        print(dishes_data)
        return JsonResponse({'dishes': dishes_data, 'query': query})

    # Convert the dishes queryset to a list of dictionaries
    # dishes_data = [{"id": dish.id, "name": dish.dish_name, "price": dish.price} for dish in dishes]
    
    # return JsonResponse({'dishes': dishes_data, 'query': query})


class resView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get(self, request, pk):
        if pk==0:
            res=Restaurant.objects.all()
        else:
            res = Restaurant.objects.filter(pk=pk)
        ser = resSerializer(res, many=True)
        return Response(ser.data)

    def post(self, request, pk):
        ser = resSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ser = Restaurant.objects.get(pk=pk)
        ser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        items = Restaurant.objects.get(pk=pk)
        ser = resSerializer(items, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class dishView(APIView):
    permission_classes = [IsResAdmin]

    def get(self, request, pk=None):
        if pk!=0:
            try:
                dish = Dish.objects.get(pk=pk)
                ser = dishSerializer(dish)
            except Dish.DoesNotExist:
                return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            dish = Dish.objects.all()
            ser = dishSerializer(dish, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = dishSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            dish = Dish.objects.get(pk=pk)
            self.check_object_permissions(request, dish)
            dish.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dish.DoesNotExist:
            return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            dish = Dish.objects.get(pk=pk)
            self.check_object_permissions(request, dish)
            ser = dishSerializer(dish, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dish.DoesNotExist:
            return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)
from django.http import JsonResponse

def getDishes(request, pk):
    try:
        dishes = Dish.objects.filter(restaurant_id=pk)
        ser = dishSerializer(dishes, many=True)
        return JsonResponse(ser.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

        