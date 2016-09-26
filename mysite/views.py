from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'mysite/home.html',{'counter':['set_home']})
	# return HttpResponse('<h2>This is the home page</h2>')

def contact(request):
	return render(request,'mysite/contact.html', {'counter':['set_contact']})

def about_website(request):
	return render(request,'mysite/about_website.html',{'counter':['set_about_website']})

def site_map(request):
	return render(request,'mysite/sitemap.xml',{'counter':['set_site_map']},content_type='text/xml')