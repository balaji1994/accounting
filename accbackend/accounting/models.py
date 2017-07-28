from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Users(models.Model):
	account_no = models.IntegerField(blank=True,null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	login_token = models.CharField(max_length=200,blank=True,null=True)
	phonenumber = models.CharField(max_length=20)
	password = models.CharField(max_length=500)
	state = models.CharField(default="",max_length=200)
	city = models.CharField(default="",max_length=200)
	postcode = models.CharField(default="",max_length=200)
	is_active = models.IntegerField(default=0)
	is_delete = models.IntegerField(default=0)

	def __str__(self):
		return self.last_name

	class Meta:
		ordering =('id',)