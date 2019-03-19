from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mainpage.models import *

class UserProfileForm(forms.ModelForm):
    Rank = models.CharField(widget=forms.HiddenInput(), initial='None')
    RankScore = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model=UserProfile
        fields=('avatar')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password','first_name', 'last_name')

        
class PictureForm(forms.ModelForm):
    TruthVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    FalseVotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    Date = forms.DateField(help_text = "Please enter the date you took the photo")
    Location = forms.CharField(max_length=128,help_text="Please enter the location you took the photo")
    class Meta:
        model = Picture
        exclude=('UserID')

class CommentsForm(forms.ModelForm):
    Text = forms.CharField(max_length=128, help_text = "Please enter the comments")
    class Meta:
        model = Comments
        exclude= ('User', 'Picture')

#FORMS BY HUGO: , decide which ones to keep, merge, delete --->

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

    class Meta:
        model = Picture
        fields = ("picture", "description")

