"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from posts.views import home_page,get_blog_post,get_blog_posts,create,update,delete,search,view_blog_post
from django.conf import settings


urlpatterns = [
    path('home/', home_page),
    path('home/<str:slug>/',get_blog_post),
    path('blog/<str:slug>/',view_blog_post),
    path('blog/',get_blog_posts),
    path('create/',create),
    path('update/<str:slug>/',update),
    path('delete/<str:slug>/',delete),
    path('search/',search),
    path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)