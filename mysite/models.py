from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	contact_name = models.CharField(max_length=50)
	contact_email = models.EmailField()
	content = models.CharField(max_length=500)

	def __str__(self):
		return self.contact_name
