from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class contant(models.Model):
	name=models.CharField(max_length=40)
	email=models.EmailField(max_length=70)
	mobno=models.CharField(max_length=25)
	desc=models.CharField(max_length=400)

class blogpost(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=50)
	desc=models.CharField(max_length=5000)
	img=models.ImageField(upload_to='blog/images')
	date=models.DateTimeField(auto_now_add=True)