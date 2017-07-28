from rest_framework import serializers
from datetime import datetime
from accounting.models import (Users)

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('id', 'first_name', 'email')



class Signup(serializers.ModelSerializer):

	class Meta:
		model = Users
		fields = '__all__'