from django.conf.urls import url
from django.views.generic import ListView,DetailView
from .models import Project
# or from projects.models import Project

urlpatterns=[
	url(r'^$',ListView.as_view(queryset=Project.objects.all().order_by("-date")[:25],template_name=\
	'projects/projects.html')),
	# url(r'^(?P<pk>\d+)/$',DetailView.as_view(model=Project,template_name='projects/project.html')),
	url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$',DetailView.as_view(model=Project,template_name='projects/project.html')),
]
