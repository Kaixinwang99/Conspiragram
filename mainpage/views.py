from django.shortcuts import render

def index(request):
	request = render(request, 'mainpage/index.html', context={})
	return request
	
def about(request):
	request = render(request, 'mainpage/about.html', context={})
	return request
	
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
	
def mainpage(request):
	request = render(request, 'mainpage/mainpage.html', context={})
	return request