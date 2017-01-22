from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^sup3rs3cr3t/', include(admin.site.urls)),
    url(r'^',include('mysite.urls')),
    url(r'^markdown/',include('django_markdown.urls')),
    url(r'^projects/',include('projects.urls')),
    url(r'^blog/',include('posts.urls')),
    url(r'^about/me/',include('mysite.urls')),
    url(r'^contact/',include('mysite.urls')),
    url(r'^sitemap.xml/',include('mysite.urls')),
)
