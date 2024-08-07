# from django.shortcuts import render, redirect,reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# # from restuarant.models import *
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user,"---------------------------------")
#         if user is not None:
#             login(request, user)
#             return redirect('home')  # Redirect to a success page.
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'login.html')
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page.
#
#
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def home_view(request):
#     return render(request, 'home.html')
#
# # def search(request,item):
#
#
# from django.views.generic.edit import CreateView
# from .forms import UserForm
# from django.contrib.auth.models import User
# from.models import Profile
# class UserCreateView(CreateView):
#     model = User
#     form_class = UserForm
#     template_name = 'signup.html'
#     success_url = '/login'
#
#     def form_valid(self, form):
#         # Save the user first
#         user = form.save()
#         print(user)
#         # Save the mobile number or handle additional logic here if necessary
#         mobile = form.cleaned_data.get('mobile')  # Assuming a profile model with a mobile field
#         m=Profile(mobile=mobile,user_id=user.id)
#         m.save()
#
#
#         return super().form_valid(form)
#
# def search_(request):
#     query = request.GET.get('query', '')
#     dishes = Dish.objects.filter(dish_name__icontains=query)
#     print(dishes)
#     restaurant=  Restaurant.objects.filter(name__icontains=query)
#     print(restaurant)
#     return render(request,'home.html',context= {'dishes': dishes,'restaurant':restaurant,'query': qf
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User
from rest_framework import authentication, permissions

from .serializers import userSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.conf import settings
from django.http import HttpResponseRedirect


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )

class users(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
