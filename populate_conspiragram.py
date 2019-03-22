import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'conspiragram.settings')
import django
django.setup()
from mainpage.models import User, Picture, Comment, Rating

def populate():
	users = [
		{"ID": "DDD@example.com",
                "avatar": "user_pictures/profile1.jpg",
		"fname": "Dave",
                "lname": "Strider",
		"date": "2015-02-03",
		"isstaff": "False"},
		{"ID": "Shauna239@example.com",
                "avatar": "user_pictures/profile2.jpg",
		"fname": "Shauna",
                "lname": "Shining",
		"date": "2015-12-23",
		"isstaff": "False"},
		{"ID": "theworst@example.com",
                "avatar": "user_pictures/profile3.jpg",
		"fname": "The",
                "lname": "Worst",
		"date": "2016-06-15",
		"isstaff": "False"},
		{"ID": "theworst2@example.com",
                "avatar": "user_pictures/profile3.jpg",
		"fname": "Not",
		"lname": "AnAlt",
                "date": "2016-06-15",
		"isstaff": "False"},
		{"ID": "prolificposter@example.com",
                "avatar": "user_pictures/profile4.jpg",
		"fname": "Prolific",
                "lname": "Poster",
		"date": "2014-05-28",
		"isstaff": "True"}
	]
	pictures = [
		{"author": "Shauna239@example.com",
		"picture": "user_pictures/ufo3.jpg",
		"date": "2018-06-20",
		"description": "UFO spotted near Edinburgh",
                "truth_rating": 2,
                "false_rating": 3,
                "verified_rating": 2},
		{"author": "prolificposter@example.com",
		"picture": "user_pictures/bigfoot.jpeg",
		"date": "2016-02-01",
                "description": "Original Bigfoot Photo",
		"location": "California",
                "truth_rating": 4,
                "false_rating": 3,
                "verified_rating": 25},
		{"author": "theworst@example.com",
                "picture": "user_pictures/ufo1.jpg",
		"date": "2019-03-13",
		"description": "REAL UFO OUTSIDE MY HOUSE",
                "truth_rating": 2,
                "false_rating": 4,
                "verified_rating": 0},
		{"author": "DDD@example.com",
		"picture": "user_pictures/lochness.jpg",
		"date": "2016-08-01",
		"description": "Loch Ness Monster",
                "truth_rating": 4,
                "false_rating": 1,
                "verified_rating": 40}
	]
	comments = [
		{"author": "theworst@example.com",
		"picauthor": "Shauna239@example.com",
		"comment": "lol fake",
		"date": "2019-03-15"},
		{"author": "theworst@example.com",
		"picauthor": "DDD@example.com",
		"comment": "obv not real",
		"date": "2019-03-15"},
		{"author": "theworst@example.com",
		"picauthor": "prolificposter@example.com",
		"comment": "lollllll fakeeeee",
		"date": "2019-03-15"},
		{"author": "theworst2@example.com",
		"picauthor": "theworst@example.com",
		"comment": "best pic on here keep up the good work",
		"date": "2019-03-15"},
		{"author": "prolificposter@example.com",
		"picauthor": "Shauna239@example.com",
		"comment": "could be real but that's really out of focus!",
		"date": "2019-03-16"},
		{"author": "DDD@example.com",
		"picauthor": "DDD@example.com",
		"comment": "the original conspiracy!",
		"date": "2019-03-16"}
	]
	for u in users:
		print("hi")
		add_user(u["ID"], u["fname"], u["lname"], u["date"], u["isstaff"])
	for p in pictures:
		print("test")
		add_picture(p["author"], p["picture"], p["description"], p["date"])
		add_rating(p["author"], p["truth_rating"], p["false_rating"], p["verified_rating"])
	for c in comments:
		add_comment(c["author"], c["picauthor"], c["comment"], c["date"])
	
	
def add_user(id, fname, lname, date, isstaff):
	u = User.objects.get_or_create(email=id)[0]
	u.first_name = fname
	u.last_name = lname
	u.date_joined = date
	u.is_staff = isstaff
	u.save()
	return u
	
def add_picture(author, picture, desc, date):
	p = Picture.objects.get_or_create(author = User.objects.get(email=author), picture = picture)[0]
	p.description = desc
	p.date_published = date
	p.save()
	return p
	
def add_comment(author, picauthor, comment, date):
	c = Comment.objects.get_or_create(author = User.objects.get(email=author), picture = Picture.objects.filter(author=User.objects.get(email=picauthor)).first())[0]
	c.comment = comment
	c.date_published = date
	c.save()
	return c

def add_rating(author, true, false, verif):
        r = Rating.objects.get_or_create(author = User.objects.get(email=author), picture = Picture.objects.filter(author=User.objects.get(email=author)).first())[0]
        r.truth_rating = true
        r.fake_rating = false
        r.verified_rating = verif
        r.save()
        return r
	
if __name__ == '__main__':
	print("Starting Conspiragram population script...")
	populate()
