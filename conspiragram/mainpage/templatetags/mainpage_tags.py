from django import template
from mainpage.models import *

import datetime
from django.utils import timezone

register = template.Library()


@register.assignment_tag
def get_pic_ratings(picture):
    ratings = Rating.objects.filter(picture=picture)

    truth_sum = 0
    fake_sum = 0
    verified_sum = 0

    if len(ratings) == 0:
        return {"truth": 0,
                "fake": 0,
                "verified": 0}

    for rating in ratings:
        truth_sum += rating.truth_rating
        fake_sum += rating.fake_rating
        verified_sum += rating.verified_rating

    return {"truth": truth_sum//len(ratings),
            "fake": fake_sum//len(ratings),
            "verified": verified_sum//len(ratings)}

@register.assignment_tag
def get_current_user_pic_ratings(user, picture):
    rating = Rating.objects.filter(author=user, picture=picture)

    if len(rating) == 0:
        return {"truth": 0,
                "fake": 0,
                "verified": 0}

    rating = rating[0]

    return {"truth": rating.truth_rating,
            "fake": rating.fake_rating,
            "verified": rating.verified_rating}

@register.assignment_tag
def get_user_uploads(user):
    return Picture.objects.filter(author=user).order_by("-date_published")


@register.assignment_tag
def get_picture_comments(picture):
    return Comment.objects.filter(picture=picture).order_by("date_published")


@register.assignment_tag
def get_date_posted(picture):
    posted = picture.date_published
    now = timezone.now()

    difference = now - posted

    if difference > datetime.timedelta(days=2):
        return str(difference.days) + " days ago"
    elif difference > datetime.timedelta(days=1):
        if posted.minute < 10:
            return "Yesterday at %s:%s" % (posted.hour, "0" + str(posted.minute))
        else:
            return "Yesterday at %s:%s" % (posted.hour, posted.minute)
    elif difference > datetime.timedelta(seconds=3600):
        return "%s hours ago" % (difference.seconds // 3600)
    elif difference > datetime.timedelta(seconds=60):
        return "%s minutes ago" % (difference.seconds // 60)
    else:
        return "About a minute ago"


@register.assignment_tag
def get_position(picture, feed):
    counter = 0

    for pic in feed:
        if pic == picture:
            return counter
        counter += 1

    return -1

@register.assignment_tag
def get_user_stats(user):
    pictures = Picture.objects.filter(author=user)

    truth_sum = 0
    fake_sum = 0
    verified_sum = 0

    if len(pictures) == 0:
        return {"truth": 0,
                "fake": 0,
                "verified": 0}

    for picture in pictures:
        pic_stats = get_pic_ratings(picture)
        truth_sum += pic_stats["truth"]
        fake_sum += pic_stats["fake"]
        verified_sum += pic_stats["verified"]

    return {"truth": truth_sum//len(pictures),
            "fake": fake_sum//len(pictures),
            "verified": verified_sum//len(pictures)}

