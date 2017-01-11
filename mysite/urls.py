from django.conf.urls import url

from .views import home,contact,about_website,site_map

urlpatterns=[
	url(r'^$',home,name='home'),
	url(r'^contact/$',contact,name='contact'),
	url(r'^about/website/$',about_website,name='about_website'),
	url(r'^sitemap.xml/$',site_map,name='site_map'),
]
