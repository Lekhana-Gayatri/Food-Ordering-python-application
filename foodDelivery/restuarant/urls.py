from django.urls import path
from .views import *

urlpatterns = [
    # path('search/', search, name='search'),
    # path('menu_list/', menu_list, name='menu_list'),
    # path('login/', restaurant_login, name='restaurant_login'),
    # path('update_dish/<int:id>', update_dish, name='update_dish'),
    # path('delete_dish/<int:id>', delete_dish, name='delete_dish'),
    # path('res/logout', restaurant_logout, name='restaurant_logout'),
    path('/res/<int:pk>',resView.as_view()),
    path('dish/<int:pk>',dishView.as_view()),
    path('/hello',hello,name='hello'),
]
