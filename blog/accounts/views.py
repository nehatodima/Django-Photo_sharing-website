
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

#from blog import templates

def registrationview(request):
	if(request.method == "POST"):
		user=User.objects.create_user( request.POST['username'], password=request.POST['password1'])
		user.save()
		login(request,user)
		form = UserCreationForm(request.POST)
		return redirect('../../home')
	else:
		form = UserCreationForm()
	context = {"form" : form}
	return render(request,"registration/register.html",context)


def loginview(request):
	if(request.method == "POST"):
		user=authenticate(request,username = request.POST['username'],password = request.POST['password'])
		if user is None:
			return render(request,'registration/login.html',{'form' : AuthenticationForm(),'error':'Invalid username or password'})
		else:
			login(request,user)
			return redirect('../../home')
	else:
	    return render(request,"registration/login.html",{'form' : AuthenticationForm()})   
	

def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("../../home/")


