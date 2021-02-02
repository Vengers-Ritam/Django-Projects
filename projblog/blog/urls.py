from django.urls import path
from . import views

urlpatterns=[
		path('', views.main,name='main'),
		path('login/',views.ulogin,name='login'),
		path('crudpost/',views.crudpost,name='crudpost'),
		path('registration/',views.regis_form,name='registration'),
		path('profile/',views.uprofile,name='profile'),
		path('about/',views.uabout,name='about'),
		path('contant/',views.ucontant,name='contant'),
		path('logout/',views.ulogout,name='logout'),
		path('addpost/',views.addpost,name='addpost'),
		path('editpost/<int:id>',views.editpost,name='editpost'),
		path('delete/<int:id>',views.delpost,name='deletepost'),
		path('changepassword/',views.changepass,name='changepassword')
]