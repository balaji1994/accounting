from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Users(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	phonenumber = models.CharField(max_length=20)
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.last_name

	class Meta:
		ordering =('id',)