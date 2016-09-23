from django.conf.urls import url

from .views import home,contact,about_website

urlpatterns=[
	url(r'^$',home,name='home'),
	url(r'^contact/$',contact,name='contact'),
	url(r'^about/website/$',about_website,name='about_website'),
]