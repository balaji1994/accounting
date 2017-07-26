from django.contrib import admin

# Register your models here.

from accounting.models import Users

admin.site.register(Users)