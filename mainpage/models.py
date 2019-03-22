from __future__ import unicode_literals
import itertools

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from datetime import *
from django.utils import timezone
from mainpage.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    avatar = models.ImageField(upload_to='user_uploads', null=True)
    slug = models.SlugField(default="", unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateField(_("Date"), default=date.today)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def save(self, *args, **kwargs):
        slug = slugify(self.get_full_name())

        for i in itertools.count(1):
            if not User.objects.filter(slug=slug).exists():
                break
            slug = slugify(str(self))
            slug = '%s%d' % (slug, i)

        self.slug = slug
        super(User, self).save(*args, **kwargs)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    def __str__(self):
        return self.get_full_name()

class Picture(models.Model):

    author = models.ForeignKey(User)
    picture = models.ImageField(upload_to="user_uploads", blank=True, null=True)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        if str(self.author)[-1] == "s":
            return str(self.author) + "' picture"
        else:
            return str(self.author) + "'s picture"

    def save(self, *args, **kwargs):
        slug = slugify(str(self))

        for i in itertools.count(1):
            if not Picture.objects.filter(slug=slug).exists():
                break
            slug = slugify(str(self))
            slug = '%s%d' % (slug, i)

        self.slug = slug
        super(Picture, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    comment = models.TextField()
    date_published = models.DateTimeField(default=timezone.now())

class Rating(models.Model):
    author = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    truth_rating = models.PositiveIntegerField(default=0)
    fake_rating = models.PositiveIntegerField(default=0)
    verified_rating = models.BooleanField(default = False)
    

