from datetime import datetime

from mainpage.models import *
from mainpage.forms import *

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
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

    # context_dict={}
    request.session.set_test_cookie()
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    # request = render(request, 'mainpage/index.html', context_dict)

    if request.user.is_authenticated():
        return redirect("foodfeed")

    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        login_form = LogInForm(request.POST)

        if sign_up_form.is_valid() and request.POST.get("submit") == "Sign Up":
            sign_up_form.save()
            user_email = sign_up_form.cleaned_data.get("email")
            user_password = sign_up_form.cleaned_data.get("password1")

        elif request.POST.get("submit") == "Login":
            user_email = request.POST.get("email")
            user_password = request.POST.get("password")

        user = authenticate(email=user_email, password=user_password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("foodfeed")

    else:
        sign_up_form = SignUpForm()
        login_form = LogInForm()

    return render(request, "foodfeed/index.html", {"sign_up_form": sign_up_form,
                                                   "login_form": login_form})

	
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

@login_required(login_url="index")
def mainpage(request):
    feed = Picture.objects.order_by("-date_published")
	
    if request.user.is_authenticated():
        request = render(request, 'mainpage/mainpage.html', context={})
        return request
    else:
        context_dict={}
        equest = render(request, 'mainpage/index.html', context_dict)
        return request

    if request.method == "POST":
        if request.POST.get("submit") == "Sign Out":
            logout(request)
            return redirect("index")

        elif request.POST.get("submit") == "Upload":
            upload_form = ImageUploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                new_picture = Picture(author=request.user,
                                      picture=request.FILES["picture"],
                                      description=request.POST["description"])
                new_picture.save()
                return redirect("mainpage")

        elif request.POST.get("submit") == "Comment":
            new_comment = Comment(author=request.user,
                                  picture=Picture.objects.get(slug=request.POST["picture"]),
                                  comment=request.POST["comment"])
            new_comment.save()
            return redirect("mainpage")

    else:
        upload_form = ImageUploadForm()
        comment_form = CommentSubmissionForm()

    return render(request, "mainpage/mainpage.html", {"feed": feed,
                                                      "upload_form": upload_form,
                                                      "comment_form": comment_form})
def add_comment(request):
    if request.is_ajax():
        new_comment = Comment(author=request.user,
                              picture=Picture.objects.get(slug=request.GET.get("picture_slug", "")),
                              comment=request.GET.get("comment", ""))
        new_comment.save()

        return HttpResponse("")
    else:
        raise Http404




	
