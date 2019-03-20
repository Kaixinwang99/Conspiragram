from django.shortcuts import render
from datetime import datetime
from mainpage.models import Picture,Comments,UserProfile
#from mainpage.forms import
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val
def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        #update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())

    else:
        # set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
    # Update/set the visits cookie
    request.session['visits'] = visits
    
def index(request):
        context_dict={}
        request.session.set_test_cookie()
        visitor_cookie_handler(request)
        context_dict['visits'] = request.session['visits']
        request = render(request, 'mainpage/index.html', context_dict)
        return request
	
def about(request):
        context_dict={}
        visitor_cookie_handler(request)
        context_dict['visits']=request.session['visits']
        request = render(request, 'mainpage/about.html', context_dict)
        return request
	
def restricted(request):
        return HttpResponse("Since you're logged in, you can see this text!")

def profile_edit(request):
	request = render(request, 'mainpage/profile_edit.html', context={})
	return request

def user_profile(request, user_profile_slug):

    try:
        userprofile = UserProfile.objects.get(slug=user_name_slug)
        context_dict['UserProfile'] = userprofile
    except UserProfile.DoesNotExist:
        context_dict['UserProfile'] = None
    request = render(request, 'mainpage/user_profile.html', context_dict)
	return request

#@login_required
def mainpage(request):
	if request.user.is_authenticated():
		request = render(request, 'mainpage/mainpage.html', context={})
		return request
	else:
		context_dict={}
		request = render(request, 'mainpage/index.html', context_dict)
		return request


	
