from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Dish, Restaurant
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .decorators import restaurant_login_required

@restaurant_login_required
def search(request):
    query = request.GET.get('query', '')
    dishes = Dish.objects.filter(Q(restaurant=request.restaurant) & Q(dish_name__icontains=query)) if query else Dish.objects.filter(restaurant=request.restaurant)

    return render(request, 'menu_list.html', {'dishes': dishes, 'query': query})

def restaurant_login(request):
    if request.method == 'POST':
        admin_username = request.POST['username']
        name = request.POST['rname']
        PasswordInput = request.POST['password']

        try:
            restaurant = Restaurant.objects.get(Q(name=name) & Q(resturant_admin=admin_username))
            if restaurant.check_password(password):
                request.session['restaurant_id'] = restaurant.id
                print(request.restaurant)
                dishes = Dish.objects.filter(restaurant_id=request.restaurant)
                return redirect('/res/menu_list/', context={'dishes': dishes})

            else:
                messages.error(request, 'Incorrect password.')
        except Restaurant.DoesNotExist:
            messages.error(request, 'Invalid Admin.')
    return render(request, 'reslogin.html')

@restaurant_login_required
def menu_list(request):
    if request.method == "POST":
        data = request.POST
        dish_name = data.get('dish_name')
        price = data.get('price')
        description = data.get('description')
        veg = data.get('veg') == 'True'  # Convert string to boolean
        discount = data.get('discount')
        dish_img=request.FILES.get('dish_img')
        d = Dish(
            dish_name=dish_name,
            price=price,
            description=description,
            veg=veg,
            discount=discount,
            restaurant_id=request.restaurant,
            dish_img=dish_img
        )
        d.save()
        dishes = Dish.objects.filter(restaurant_id=request.restaurant)
        print(dishes,"*"*100,request.restaurant)
        return redirect(reverse('menu_list'), context={'dishes': dishes})
    dishes = Dish.objects.filter(restaurant_id=request.restaurant)
    return render(request, 'menu_list.html', context={'dishes': dishes})

@restaurant_login_required
def delete_dish(request, id):
    if request.method=='POST':
        queryset = Dish.objects.get(id=id)
        print(queryset)
        queryset.delete()
    dishes = Dish.objects.filter(restaurant_id=request.restaurant)
    return redirect('/res/menu_list/', context={'dishes': dishes})

@restaurant_login_required
def update_dish(request, id):
    queryset = Dish.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        dish_name = data.get('dish_name')
        dish_img=request.FILES.get('dish_img')
        price = data.get('price')
        description = data.get('description')
        veg = data.get('veg')
        discount = data.get('discount')
        queryset.dish_name = dish_name
        queryset.price = price
        queryset.description = description
        queryset.veg = veg
        queryset.discount = discount
        if dish_img:
            queryset.dish_img=dish_img
        queryset.save()
        return redirect('/res/menu_list/')
    context = {'dish': queryset}

    dishes = Dish.objects.filter(restaurant_id=request.restaurant)
    return render(request, 'menu_list.html', context={'dishes': dishes})


@restaurant_login_required
def restaurant_logout(request):
    # Clear the restaurant session data
    if 'restaurant_id' in request.session:
        del request.session['restaurant_id']

    # Optionally, log out the user if using Django's auth system
    if request.user.is_authenticated:
        auth_logout(request)

    # Redirect to the login page or home page
    return redirect('/res/login')
