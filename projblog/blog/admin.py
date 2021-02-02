from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(contant)
class contantadmin(admin.ModelAdmin):
	list_display=['id','name','email','mobno','desc']

@admin.register(blogpost)
class blogpostadmin(admin.ModelAdmin):
	list_display=['id','title','desc','img','user']