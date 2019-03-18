from django import forms
from django.contrib.auth.models import User
from rango.models import Picture, Comments, UserProfile
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

