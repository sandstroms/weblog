from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
	"""The home page for Weblog. Shows all blog posts."""
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'weblogs/index.html', context)

def new_post(request):
	"""The page for a user to add a new post."""
	if request.method != 'POST':
		form = BlogPostForm()
	else:
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('weblogs:index'))
			
	context = {'form': form}
	return render(request, 'weblogs/new_post.html', context)
	
def my_posts(request):
	"""The page for a user to view and edit their own posts."""
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'weblogs/my_posts.html', context)
	
def edit_post(request, post_id):
	"""The page for a user to edit a selected post."""
	post = BlogPost.objects.get(id=post_id)
	
	if request.method != 'POST':
		# Initial request; pre-fill the form with the current post.
		form = BlogPostForm(instance=post)
	else:
		# POST data submitted; change the post.
		form = BlogPostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('weblogs:my_posts'))
			
	context = {'post': post, 'form': form}
	return render(request, 'weblogs/edit_post.html', context)
