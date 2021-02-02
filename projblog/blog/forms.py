from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .models import *

class uform(UserCreationForm):
	password1=forms.CharField(label='Create Your Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2=forms.CharField(label='Re-type Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email Address'}
		widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
				'first_name':forms.TextInput(attrs={'class':'form-control'}),
				'last_name':forms.TextInput(attrs={'class':'form-control'}),
				'email':forms.TextInput(attrs={'class':'form-control'})}

class uloginform(AuthenticationForm):
	username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password=forms.CharField(label=_("Password"),
							strip=False,
							widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))

class upostform(UserChangeForm):
	password=None
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']
		labels={'email':'Email'}
		widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
				'first_name':forms.TextInput(attrs={'class':'form-control'}),
				'last_name':forms.TextInput(attrs={'class':'form-control'}),
				'email':forms.TextInput(attrs={'class':'form-control'})}

class contantusform(forms.ModelForm):
	class Meta:
		model=contant
		fields='__all__'
		widgets={'desc':forms.Textarea(attrs={'class':'form-control'}),
				'mobno':forms.TextInput(attrs={'class':'form-control'}),
				'email':forms.TextInput(attrs={'class':'form-control'}),
				'name':forms.TextInput(attrs={'class':'form-control'})}

class blogpostform(forms.ModelForm):
	class Meta:
		model=blogpost
		fields=['title','desc','img']
		widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
				'desc':forms.Textarea(attrs={'class':'form-control'})}
		labels={'img':''}





