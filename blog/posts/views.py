from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import BlogPost
from blog.forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from blog import templates

def home_page(request):
	s = '';
	qs = '';
	if(request.user.get_username() != ''):
		qs = BlogPost.objects.filter(usersname = request.user)  
		s = request.user.get_username()  
	context = {"username" : s , "object_list" : qs}	
	return render(request,"home.html",context)


def get_blog_post(request,slug):
	obj = get_object_or_404(BlogPost ,slug = slug)
	context = {"object" : obj } 
	return render(request,"blogpostdetail.html",context)

def view_blog_post(request,slug):
	obj = get_object_or_404(BlogPost ,slug = slug)
	context = {"object" : obj } 
	return render(request,"blogpostview.html",context)

def get_blog_posts(request):
	qs = BlogPost.objects.all()
	context = {"object_list" : qs } 
	return render(request,"blogposts.html",context)

@login_required
def create(request):
	form = BlogPostModelForm(request.POST or None ,request.FILES or None)
	if form.is_valid():
		BlogPost.objects.create(**form.cleaned_data,usersname = request.user)
		form = BlogPostModelForm()
		return redirect("/home")
	context = {"form" : form}
	return render(request,"create.html",context)

@login_required
def update(request,slug):
	obj = get_object_or_404(BlogPost ,slug = slug)
	form = BlogPostModelForm(request.POST or None ,instance = obj)
	if form.is_valid():
		form.save()
		form = BlogPostModelForm()
		return redirect("/home")
	context = {"form" : form}
	return render(request,"create.html",context)

@login_required
def delete(request,slug):
	obj = get_object_or_404(BlogPost ,slug = slug)
	if(request.method == "POST"):
		obj.delete()
		return redirect("/blog")
	context = {"object" : obj }
	return render(request,"delete.html",context)

def search(request):
	query = request.GET.get('q',None)
	postlist = BlogPost.objects.filter(title = query)
	context = {"query" : query, "postlist" : postlist}
	return render(request,"searchpost.html",context)
