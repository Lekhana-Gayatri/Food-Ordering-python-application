from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('search_/', views.search_, name='search_'),

]