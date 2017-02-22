from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sup3rs3cr3t/', include(admin.site.urls)),
    url(r'^',include('mysite.urls')),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^blog/',include('posts.urls')),
)
