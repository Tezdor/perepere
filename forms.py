from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'username', 'email', 'password1', 'password2']
        

class BookingForm(forms.ModelForm):
    data = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Booking
        fields = ['nyanya', 'payment_method', 'data']
