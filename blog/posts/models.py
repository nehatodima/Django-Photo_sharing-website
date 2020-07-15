from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	image = models.ImageField(upload_to = 'image/',blank = True, null = True)
	title = models.CharField(max_length = 120);
	slug = models.SlugField(unique = True,default = "addslug" )
	content = models.TextField(null=True);
	usersname = models.ForeignKey(User,on_delete=models.CASCADE)
	#usersname = models.TextField(null=True);
	



	#def __str__(self):
	#	return self.title

