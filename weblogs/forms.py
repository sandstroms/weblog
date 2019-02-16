from django import forms

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'body']
		labels = {'title': 'Title', 'body': ''}
		widgets = {'body': forms.Textarea(attrs={'cols': 80})}
