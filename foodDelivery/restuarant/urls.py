from django.urls import path
from .views import *

urlpatterns = [
    path('/res/<int:pk>',resView.as_view()),
    path('dish/<int:pk>',dishView.as_view()),
    ]