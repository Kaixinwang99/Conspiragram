from django.contrib import admin
from rango.models import Picture,Comments
from rango.models import UserProfile

#I just did a sample code you can change and fix it as you wish
class PictureAdmin(admin.ModelAdmin):
    list_display = ("picture", "description", "TruthVotes", "FalseVotes", "Location")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('Text')

class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('User.username')}
    
admin.site.register(Picture, PictureAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
