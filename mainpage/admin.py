from django.contrib import admin
from mainpage.models import *

#I just did a sample code you can change and fix it as you wish
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    prepopulated_fields = {"slug": ("first_name", "last_name")}

class PictureAdmin(admin.ModelAdmin):
    list_display = ("author", "slug",)
    prepopulated_fields = {"slug": ("author", )}

class RatingAdmin(admin.ModelAdmin):
    list_display = ("author", "picture", "truth_rating", "fake_rating", "verified_rating")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "picture", "comment", "date_published")
    
admin.site.register(User, UserAdmin)
admin.site.register(Picture, PictureAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)

