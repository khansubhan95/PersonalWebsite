from __future__ import unicode_literals

from django.db import models
from django_markdown.models import MarkdownField 

# Create your models here.

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=140)
    # body = models.TextField(max_length=10000) 
    date = models.DateTimeField()
    '''
    image with image field
    '''
    # image = models.ImageField(upload_to='img/',null=True,blank=True)

    '''
    image with url
    '''
    image = models.CharField(max_length=500, blank=True)
    # slug = models.SlugField(max_length=140, unique=True)
    link = models.CharField(max_length=200)
    published = models.BooleanField(default=True)

    objects = PostManager()

    def __str__(self):
        return self.title
