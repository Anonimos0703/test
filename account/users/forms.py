# users/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     first_name = forms.CharField(max_length=30)
#     last_name = forms.CharField(max_length=30)
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(),
#         help_text = ''
#     )
     

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#         help_texts = {
#             'username' :None,
#             'password2': None,
#         }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text = ''
    )

    class Meta:
        model = CustomUser  # Use the custom user model
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password2': None,
        }
