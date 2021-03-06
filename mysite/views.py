from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Contact
from posts.models import Post
# Create your views here.

def home(request):
	queryset = Post.objects.filter(published=True).order_by("-date")[:2]
	return render(request,'mysite/home.html',{'posts': queryset})
	# return HttpResponse('<h2>This is the home page</h2>')

def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			contact_name=request.POST.get('contact_name','')
			contact_email=request.POST.get('contact_email','')
			content=request.POST.get('content','')
			#to_be_sent=contact_name+' sent you an email from '+contact_email\
			#+' content:\n'+content
			#status=send_mail(subject='Email from viewer of your site!',\
			# 	message=to_be_sent,\
			# 	from_email=None,\
			# 	recipient_list=['khansubhan20@yahoo.com'],\
			#	fail_silently=False,)
			#if status:
			# 	return render(request,'mysite/contact_success.html')
			#else:
			#	return render(request,'mysite/contact_failure.html')
			try:
				Contact.objects.create(contact_name=contact_name, contact_email=contact_email, content=content)
				return render(request, 'mysite/contact_success.html')
			except:
				return render(request, 'mysite/contact_failure.html')
	return render(request,'mysite/contact.html', \
		{'counter':['set_contact'],'form':ContactForm})
	# return render(request,'mysite/contact.html', {'counter':['set_contact']})

def about(request):
	return render(request, 'mysite/about.html', {'counter':['set_about']})

def about_website(request):
	return render(request,'mysite/about_website.html',{'counter':['set_about_website']})

def site_map(request):
	return render(request,'mysite/sitemap.xml',{'counter':['set_site_map']},content_type='text/xml')
