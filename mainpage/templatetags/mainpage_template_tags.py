from django import template
from mainpage.models import Picture, Comments

register = template.Library()

@register.inclusion_tag('mainpage/mainpage.html')
'''
def get_date_posted():
    return
#{% get_date_posted pic as date %}
#<p class="date">{{ date }}</p>
#in mainpage.html line 36


def get_picture_comments():
    return
#{% get_picture_comments pic as comments %}
#in mainpage.html line 65


def get_position():
    return
#in mainpage.html line 42
#{% get_position pic feed as index %}


def get_current_user_pic_ratings():
    return 
#in mainpage.html line 96
#{% get_current_user_pic_ratings user pic as details %}


def get_pic_ratings():
    return
#line 159
#{% get_pic_ratings pic as details %}

def get_user_stats():
    return
#line 218
#{% get_user_stats user as stats %}
'''
