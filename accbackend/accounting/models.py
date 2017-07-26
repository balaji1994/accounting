from django.db import models

# Create your models here.


class Users(models.Model):
	first_name = models.Charfield(max_length=50)
	last_name = models.Charfield(max_length=50)
	email = models.Emailfield()
	password = models.Charfield(max_length=200)

	def __str__(self):
		return self.first_name

	class Meta:
		ordering =('id',)