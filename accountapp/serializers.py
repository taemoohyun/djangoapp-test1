from rest_framework import serializers
from .models import DBTest

class DBTestSerializer(serializers.ModelSerializer):
	class Meta:
	    model = DBTest
	    fields = ('title', 'body', 'answer')
