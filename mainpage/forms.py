from django import forms
from django.contrib.auth.forms import UserCreationForm
from mainpage.models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))
    last_name = forms.CharField(max_length=30, required=False, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))
    email = forms.EmailField(max_length=254, help_text="", widget=forms.TextInput(attrs={'class': "indexForm"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "indexForm"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "indexForm"}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")


class LogInForm(forms.ModelForm):
    email = forms.EmailField(max_length=254 , widget=forms.TextInput(attrs={'class': "indexForm"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "indexForm"}))

    class Meta:
        model = User
        fields = ("email", "password")

