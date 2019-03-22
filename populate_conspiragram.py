import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'conspiragram.settings')
import django
django.setup()
from mainpage.models import User, Picture, Comment, Rating

def populate():
	users = [
		{"ID": "DDD@example.com",
                "avatar": "profile1.jpg",
		"fname": "Dave",
                "lname": "Strider",
		"date": "2015-02-03",
		"isstaff": "False"},
		{"ID": "Shauna239@example.com",
                "avatar": "profile2.jpg",
		"fname": "Shauna",
                "lname": "Shining",
		"date": "2015-12-23",
		"isstaff": "False"},
		{"ID": "theworst@example.com",
                "avatar": "profile3.jpg",
		"fname": "The",
                "lname": "Worst",
		"date": "2016-06-15",
		"isstaff": "False"},
		{"ID": "theworst2@example.com",
                "avatar": "profile3.jpg",
		"fname": "Not",
		"lname": "AnAlt",
                "date": "2016-06-15",
		"isstaff": "False"},
		{"ID": "prolificposter@example.com",
                "avatar": "profile4.jpg",
		"fname": "Prolific",
                "lname": "Poster",
		"date": "2014-05-28",
		"isstaff": "True"}
	]
	pictures = [
		{"author": "Shauna239@example.com",
		"picture": "ufo3.jpg",
		"date": "2018-06-20",
		"description": "UFO spotted near Edinburgh",
                "truth_rating": 30,
                "false_rating": 35,
                "verified_rating": "False"},
		{"author": "prolificposter@example.com",
		"picture": "bigfoot.jpeg",
		"date": "2016-02-01",
                "description": "Original Bigfoot Photo",
		"location": "California",
                "truth_rating": 1079,
                "false_rating": 885,
                "verified_rating": "True"},
		{"author": "theworst@example.com",
                "picture": "ufo1.jpg",
		"date": "2019-03-13",
		"description": "REAL UFO OUTSIDE MY HOUSE",
                "truth_rating": 2,
                "false_rating": 380,
                "verified_rating": "False"},
		{"author": "prolificposter@example.com",
		"picture": "lochness.jpg",
		"date": "2016-08-01",
		"description": "Loch Ness Monster",
                "truth_rating": 1258,
                "false_rating": 506,
                "verified_rating": "True"}
	]
	comments = [
		{"author": "theworst@example.com",
		"picture": 0,
		"comment": "lol fake",
		"date": "2019-03-15"},
		{"author": "theworst@example.com",
		"picture": 0,
		"comment": "lol fake",
		"date": "2019-03-15"},
		{"author": "theworst@example.com",
		"picture": 0,
		"comment": "lol fake",
		"date": "2019-03-15"},
		{"author": "theworst2@example.com,
		"picture": 0,
		"comment": "best pic on here keep up the good work",
		"date": "2019-03-15"},
		{"author": "prolificposter@example.com",
		"picture": 0,
		"comment": "could be real but that's really out of focus!",
		"date": "2019-03-16"},
		{"author": "DDD@example.com,
		"picture": 0,
		"comment": "ah the original conspiracy!",
		"date": "2019-03-16"}
	]
	for u in users:
		add_user(u["ID"], u["fname"], u["lname"], u["date"], u["isstaff"])
	for p in pictures:
		add_picture(p["author"], p["picture"], p["description"], p["date"])
		add_rating(p["author"], p["picture"], p["truth_rating"], p["false_rating"], p["verified_rating"]
	for c in comments:
		add_comment(c["author"], c["picture"], c["comment"], c["date"])
	
	
def add_user(id, fname, lname, date, isstaff):
	u = User.objects.get_or_create(email=id)
	u.first_name = fname
	u.last_name = lname
	u.date_joined = date
	u.is_staff = isstaff
	u.save()
	return u
	
def add_picture(author, picture, desc, date):
	p = Picture.objects.get_or_create(author = author, picture = picture)
	p.description = desc
	p.date_published = date
	p.save()
	return p
	
def add_comment(author, picture, comment, date):
	c = Comment.object.get_or_create(author = author, picture = picture)
	c.comment = comment
	c.date_published = date
	c.save()
	return c

def add_rating(author, picture, true, false, verif):
        r = Rating.object.get_or_create(author = author, picture = picture)
        r.truth_rating = true
        r.fake_rating = false
        r.verified_rating = verif
        r.save()
        return r
	
if __name__ == '__main__':
	print("Starting Conspiragram population script...")
	populate()
