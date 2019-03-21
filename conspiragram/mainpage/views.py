from datetime import datetime

from mainpage.models import *
from mainpage.forms import *

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# A helper method
# def get_server_side_cookie(request, cookie, default_val=None):
# 	val = request.session.get(cookie)
# 	if not val:
# 		val = default_val
# 	return val
# def visitor_cookie_handler(request):
#     visits = int(get_server_side_cookie(request, 'visits', '1'))
#     last_visit_cookie = get_server_side_cookie(request,
#                                                'last_visit',
#                                                str(datetime.now()))
#     last_visit_time = datetime.strptime(last_visit_cookie[:-7],
#                                         '%Y-%m-%d %H:%M:%S')
#     # If it's been more than a day since the last visit...
#     if (datetime.now() - last_visit_time).days > 0:
#         visits = visits + 1
#         #update the last visit cookie now that we have updated the count
#         request.session['last_visit'] = str(datetime.now())

#     else:
#         # set the last visit cookie
#         request.session['last_visit'] = last_visit_cookie
#     # Update/set the visits cookie
#     request.session['visits'] = visits
    
def index(request):

    # context_dict={}
    # request.session.set_test_cookie()
    # visitor_cookie_handler(request)
    # context_dict['visits'] = request.session['visits']
    # request = render(request, 'mainpage/index.html', context_dict)

    if request.user.is_authenticated():
        return redirect("mainpage")

    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)
        login_form = LogInForm(request.POST)

        if sign_up_form.is_valid() and request.POST.get("submit") == "Sign Up":
            sign_up_form.save()
            user_email = sign_up_form.cleaned_data.get("email")
            user_password = sign_up_form.cleaned_data.get("password1")
            user = authenticate(email=user_email, password=user_password)

        elif request.POST.get("submit") == "Login":
            user_email = request.POST.get("email")
            user_password = request.POST.get("password")
            user = authenticate(email=user_email, password=user_password)
        else:
            user = authenticate(email="s", password="d")

        if user:
            if user.is_active:
                login(request, user)
                return redirect("mainpage")

    else:
        sign_up_form = SignUpForm()
        login_form = LogInForm()

    return render(request, "mainpage/index.html", {"sign_up_form": sign_up_form,
                                                   "login_form": login_form})


@login_required(login_url="index")
def mainpage(request):
    feed = Picture.objects.order_by("-date_published")

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

    if request.user.is_authenticated():
        request = render(request, 'mainpage/mainpage.html', context={})
        return request
    else:
        context_dict={}
        request = render(request, 'mainpage/index.html', context_dict)
        return request

    return render(request, "mainpage/mainpage.html", {"feed": feed,
                                                      "upload_form": upload_form,
                                                      "comment_form": comment_form})
	

@login_required(login_url="index")
def profile_edit(request):
    if request.method == "POST":
        profile_edit_form = ProfileEditForm(request.POST, request.FILES)

        for field in profile_edit_form.fields:
            if field != "avatar":
                if request.POST[field] != request.user.__getattr__(field):
                    request.user.__setattr__(field, request.POST[field])
                    request.user.save()
            elif request.FILES.__contains__("avatar"):
                request.user.avatar = request.FILES["avatar"]
                request.user.save()

        return redirect("mainpage")

    else:
        profile_edit_form = ProfileEditForm(initial={
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name})

    return render(request, "mainpage/profile_edit.html", {"form": profile_edit_form})

@login_required(login_url="index")
def user_profile(request, user_name_slug):
    if request.method == "POST":
        if request.POST.get("submit") == "Comment":
            new_comment = Comment(author=request.user,
                                  picture=Picture.objects.get(slug=request.POST["picture"]),
                                  comment=request.POST["comment"])
            new_comment.save()
            return redirect("user_profile", user_name_slug)

    else:
        comment_form = CommentSubmissionForm()

    return render(request, "mainpage/user_profile.html", {"owner": User.objects.get(slug=user_name_slug),
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

def about(request):
        # context_dict={}
        # visitor_cookie_handler(request)
        # context_dict['visits']=request.session['visits']
        # request = render(request, 'mainpage/about.html', context_dict)
        return render(request, "mainpage/about.html")


def make_rating(request):
    if request.is_ajax():
        picture = Picture.objects.get(slug=request.GET.get("picture_slug", ""))
        rating_type = request.GET.get("type", "")
        value = request.GET.get("value", "")

        try:
            rating = Rating.objects.get(author=request.user, picture=picture)

        except:
            rating = Rating.objects.create(author=request.user, picture=picture)

        if rating_type == "truth":
            rating.truth_rating = value
        elif rating_type == "style":
            rating.fake_rating = value
        else:
            rating.verified_rating = value

        rating.save()
        return HttpResponse("")

    else:
        raise Http404

def restricted(request):
        return HttpResponse("Since you're logged in, you can see this text!")

	
