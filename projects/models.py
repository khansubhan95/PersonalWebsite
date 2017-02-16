from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(published=True)

class Project(models.Model):
	title=models.CharField(max_length=140)
	heading=models.CharField(max_length=140)
	body=models.TextField()
	date=models.DateTimeField()
	slug=models.SlugField(max_length=60,blank=True)
        published = models.BooleanField(default=True)

        objects = PostManager()

	def __str__(self):
		return self.title
