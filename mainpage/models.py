from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    User = models.OneToOneField(User)
    avatar = models.ImageField(upload_to = 'profile_images',blank = True)
    Rank = models.CharField(max_length=128)
    RankScore = models.FloatField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.User.username)
        super(UserProfile, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.User.UserID

class Picture(models.Model):
    UserID = models.ForeignKey(User)
    avatar = models.ImageField(upload_to = 'user_pictures',blank = True)
    description = models.CharField(max_length=512)
    TruthVotes = models.IntegerField(default=0)
    FalseVotes = models.IntegerField(default=0)
    Date = models.DateField(auto_now_add=True)
    Location = models.CharField(max_length=128)
    PictureID = models.AutoField(primary_key = True)
    title = models.CharField(max_length=128)
    def __str__(self):
        return self.PictureID

class Comments(models.Model):
    Picture = models.ForeignKey(Picture)
    User = models.ForeignKey(User)
    Text = models.CharField(max_length=128)
    CommentID = models.AutoField(primary_key = True)
    def __str__(self):
        return self.Text
    

