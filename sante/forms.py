from django.contrib.auth.forms import UserCreationForm

from .models import Customer


class CustomerRegstrationn(UserCreationForm):
    # phone_number = forms
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone_number', 'password1', 'password2']