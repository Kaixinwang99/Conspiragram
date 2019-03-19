from django.conf.urls import url
from mainpage import views

urlpatterns = [
    url(r"^$", views.mainpage, name="mainpage"),
    url(r"^user/$", views.profile_edit, name="profile_edit"),
    url(r"^user/(?P<user_name_slug>[\w\-]+)/$", views.user_profile, name="user_profile"),
    url(r"make_rating/$", views.make_rating, name="rate"),
    url(r"add_comment/$", views.add_comment, name="comment")
]
