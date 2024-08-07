from django import forms
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    mobile = forms.CharField(label='Mobile', max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile']