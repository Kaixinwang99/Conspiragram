from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainpage.models import *

class CommentsForm(forms.ModelForm):
    comment = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': "commentInput"}))
    class Meta:
        model = Comment
        fields = ('comment',"picture")

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

class ProfileEditForm(forms.ModelForm):
    avatar = forms.ImageField(label="", required=False, widget=forms.FileInput(attrs={'class': "uploadPic"}))
    first_name = forms.CharField(max_length=30, required=False, help_text="First Name: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))
    last_name = forms.CharField(max_length=30, required=False, help_text="Last Name: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))
    email = forms.EmailField(max_length=254, help_text="Email Address: ", widget=forms.TextInput(attrs={'class': "fieldEdit"}))

    class Meta:
        model = User
        fields = ("avatar", "first_name", "last_name", "email")

class ImageUploadForm(forms.ModelForm):
    picture = forms.ImageField(label="", widget=forms.FileInput(attrs={'class': "uploadPic"}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'class': "uploadDescription"}))
    TruthVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    FalseVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    Location = forms.CharField(max_length=128,help_text="Please enter the location you took the photo")

    class Meta:
        model = Picture
        fields = ("picture", "description", "TruthVotes", "FalseVotes", "Location")

