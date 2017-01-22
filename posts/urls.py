from django.conf.urls import url
from django.views.generic import ListView,DetailView
from .models import Post
# or from blog.models import Post

urlpatterns=[
        url(r'^$',ListView.as_view(queryset=Post.objects.filter(published=True).order_by("-date")[:25],template_name=\
        'posts/posts.html')),
        # url(r'^$',ListView.as_view(queryset=Post.objects.filter(published=True).order_by("-date")[:25],template_name=\
        # 'posts/posts.html')),
        # url(r'^(?P<pk>\d+)/$',DetailView.as_view(model=Project,template_name='projects/project.html')'),
        url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$',DetailView.as_view(model=Post,template_name='posts/post.html')),
]
