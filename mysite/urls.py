from django.conf.urls import url

from .views import home,contact,about_website,site_map,about

urlpatterns=[
	url(r'^$',home,name='home'),
	url(r'^about/$', about, name='about'),
	url(r'^contact/$',contact,name='contact'),
	url(r'^sitemap.xml/$',site_map,name='site_map'),
]
