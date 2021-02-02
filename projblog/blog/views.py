from django.shortcuts import render,HttpResponseRedirect
from .forms import uform,uloginform,upostform,contantusform,blogpostform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from . models import *
from django.contrib.auth.models import User
# Create your views here.
def main(request):
	fm=blogpost.objects.all()
	return render(request,'blog/main.html',{'form':fm})

def regis_form(request):
	if request.method=='POST':
		fm=uform(request.POST)
		if fm.is_valid():
			fm.save()
			fm=uform()
	else:
		fm=uform()
	return render(request,'blog/ucreate.html',{'form':fm})

def ulogin(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			fm=uloginform(request=request,data=request.POST)
			if fm.is_valid():
				uname=fm.cleaned_data['username']
				upass=fm.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					return HttpResponseRedirect('/crudpost/')
		else:
			fm=uloginform()
		return render(request,'blog/login.html',{'form':fm})
	else:
		return HttpResponseRedirect('/crudpost/')

def crudpost(request):
	if request.user.is_authenticated:
			fm=blogpost.objects.filter(user=request.user.id)
			#print(request.user.username)
			return render(request,'blog/crudpost.html',{"fname":request.user.first_name,
				'lname':request.user.last_name,"form":fm})
	else:

		return HttpResponseRedirect('/login/')

def uprofile(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			fm=upostform(request.POST,instance=request.user)
			if fm.is_valid():
				fm.save()
		else:
			fm=upostform(instance=request.user)
		return render(request,'blog/profile.html',{'form':fm})
	else:
		return HttpResponseRedirect('/login/')

def uabout(request):
	return render(request,'blog/aboutus.html')

def ucontant(request):
	fm=contantusform(request.POST)
	if fm.is_valid():
		fm.save()
		fm=contantusform()
	else:
		fm=contantusform()
	return render(request,'blog/contantus.html',{'form':fm})

def ulogout(request):
	logout(request)
	return HttpResponseRedirect('/login/')

def addpost(request):
	if request.method=="POST":
		fm=blogpostform(request.POST,request.FILES)
		if fm.is_valid():
			nm=User(request.user.id)
			#print(nm)
			tl=fm.cleaned_data['title']
			ds=fm.cleaned_data['desc']
			img=fm.cleaned_data['img']

			adpost=blogpost(title=tl,desc=ds,img=img,user=nm)
			adpost.save()
			
	else:
		fm=blogpostform()
	return render(request,'blog/addpost.html',{'form':fm})

def editpost(request,id):
	pi=blogpost.objects.get(pk=id)
	if request.method=="POST":
		fm=blogpostform(request.POST,instance=pi)
		if fm.is_valid():
			fm.save()
	else:
		fm=blogpostform(instance=pi)
	return render(request,'blog/editpost.html',{'form':fm})

def delpost(request,id):
	dobj=blogpost.objects.get(pk=id)
	dobj.delete()
	return HttpResponseRedirect('/crudpost/')

def changepass(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			fm=PasswordChangeForm(user=request.user,data=request.POST)
			if fm.is_valid():
				fm.save()
				return HttpResponseRedirect('/profile/')
		else:
			fm=PasswordChangeForm(user=request.user)
		return render(request,'blog/changepassword.html',{'form':fm})
	else:
		return HttpResponseRedirect('/login/')






