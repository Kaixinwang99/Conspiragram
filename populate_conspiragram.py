import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					'conspiragram.settings')

import django
django.setup()
from mainpage.models import UserProfile, User, Picture, Comments

def populate():
	users = [
		{"ID": "DDD@example.com",
		"name": "DoctorDetectiveDave",
		"rank": "Expert",
		"rankscore": 83},
		{"ID": "Shauna239@example.com",
		"name": "ShaunaShining",
		"rank": "Sighter",
		"rankscore": 60},
		{"ID": "theworst@example.com",
		"name": "TheWorst",
		"rank": "None",
		"rankscore": 1},
		{"ID": "theworst2@example.com",
		"name": "NotAnAlt",
		"rank": "None",
		"rankscore": 50},
		{"ID": "prolificposter@example.com",
		"name": "ProlificPoster",
		"rank": "Expert",
		"rankscore": 92}
	]
	pictures = [
		{"UserID": "Shauna239@example",
		"true": 35,
		"false": 20,
		"date": "2018-06-20",
		"location": "Edinburgh",
		"picid": 0},
		{"UserID": "prolificposter@example",
		"true": 270,
		"false": 55,
		"date": "2018-12-25",
		"location": "London",
		"picid": 1},
		{"UserID": "theworst@example",
		"true": 1,
		"false": 358,
		"date": "2019-03-13",
		"location": "Null Island",
		"picid": 2},
		{"UserID": "prolificposter@example",
		"true": 1024,
		"false": 556,
		"date": "2016-08-01",
		"location": "Loch Ness",
		"picid": 3}
	]
	comments = [
		{"picid": 0,
		"commentid": 0,
		"userid": "theworst@example",
		"text": "lol fake"},
		{"picid": 1,
		"commentid": 0,
		"userid": "theworst@example",
		"text": "lol fake"},
		{"picid": 3,
		"commentid": 0,
		"userid": "theworst@example",
		"text": "lol fake"},
		{"picid": 2,
		"commentid": 0,
		"userid": "theworst2@example",
		"text": "best pic on here keep up the good work"},
		{"picid": 0,
		"commentid": 1,
		"userid": "DDD@example",
		"text": "could be real but that's really out of focus"},
		{"picid": 0,
		"commentid": 3,
		"userid": "DDD@example",
		"text": "Wow! This is incredible!"}
	]
	for u in users:
		add_user(u["ID"], u["name"], u["rank"], u["rankscore"])
		add_profile(u["ID"])
	for p in pictures:
		add_picture(p["UserID"], p["true"], p["false"], p["date"], p["location"], p["picid"])
	for c in comments:
		add_comment(c["picid"], c["userid"], c["commentid"], c["text"])
	
	
def add_user(id, name, rank, rankscore):
	u = User.objects.get_or_create(UserID=id)
	u.Username = name
	u.Rank = rank
	u.RankScore = rankscore
	u.save()
	return u
	
def add_profile(id, site):
	r = UserProfile.objects.get_or_create(User = id)
	r.save()
	return r
	
def add_picture(userid, true, false, date, loc, picid):
	p = Picture.objects.get_or_create(UserID = userid, PictureID = picid)
	p.TruthVotes = true
	p.FalseVotes = false
	p.Date = date
	p.Location = loc
	p.save()
	return p
	
def add_comment(picid, userid, commentid, text):
	c = Comments.object.get_or_create(Picture = picid, CommentID = commentid)
	c.UserID = userid
	c.Text = text
	c.save()
	return c
	
if __name__ == '__main__':
	print("Starting Conspiragram population script...")
	populate()