from django.conf.urls import url
from mainpage import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^mainpage/$', views.mainpage, name='mainpage'),
    url(r'^profile_edit/$', views.profile_edit, name='profile_edit'),
    
    
    
    url(r"add_comment/$", views.add_comment, name="comment"),
    url(r"^user/$", views.profile_edit, name="profile_edit"),
    url(r"^user/(?P<user_name_slug>[\w\-]+)/$", views.user_profile, name="user_profile"),




    #url(r'^add_category/$', views.add_category, name='add_category'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    #url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #    views.show_category, name='show_category'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    #url(r'^logout/$', views.user_logout, name='logout'),
]