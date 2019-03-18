from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    User = models.OneToOneField(User)
    Website = models.URLField(blank=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.User.Username)
        super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.User.UserID
    
class User(models.Model):
    UserID = models.EmailField(max_length=254, unique = True)
    Username = models.CharField(max_length=128)
    Rank = models.CharField(max_length=128)
    RankScore = models.FloatField()
    def __str__(self):
        return self.UserID

class Picture(models.Model):
    UserID = models.ForeignKey(User)
    TruthVotes = models.IntegerField(default=0)
    FalseVotes = models.IntegerField(default=0)
    Date = models.DateField(auto_now_add=True)
    Location = models.CharField(max_length=128)
    PictureID = models.IntegerField (unique = True)
    def __str__(self):
        return self.PictureID

class Comments(models.Model):
    Picture = models.ForeignKey(Picture)
    User = models.ForeignKey(User)
    Text = models.CharField(max_length=128)
    def __str__(self):
        return self.Text
    

