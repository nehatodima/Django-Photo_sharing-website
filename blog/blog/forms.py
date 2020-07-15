from posts.models import BlogPost
from django import forms
class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title','image','slug','content']
