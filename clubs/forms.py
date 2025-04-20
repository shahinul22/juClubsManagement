from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    is_organizer = forms.BooleanField(required=False, label="Are you a club organizer?")

    class Meta:
        model = User
        fields = ['username', 'email', 'is_organizer', 'password1', 'password2']
