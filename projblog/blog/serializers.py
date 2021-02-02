from rest_framework import serializers

class Stuserializer(serializers.Serializer):
	id=serializers.IntegerField()
	fname=serializers.CharField(max_length=50)
	lname=serializers.CharField(max_length=80)
	email=serializers.EmailField(max_length=100)
