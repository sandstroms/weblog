from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
	"""The home page for Weblog. Shows all blog posts."""
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'weblogs/index.html', context)

@login_required
def new_post(request):
	"""The page for a user to add a new post."""
	if request.method != 'POST':
		form = BlogPostForm()
	else:
		form = BlogPostForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('weblogs:index'))
			
	context = {'form': form}
	return render(request, 'weblogs/new_post.html', context)
	
@login_required
def my_posts(request):
	"""The page for a user to view and edit their own posts."""
	posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'weblogs/my_posts.html', context)

@login_required
def edit_post(request, post_id):
	"""The page for a user to edit a selected post."""
	post = BlogPost.objects.get(id=post_id)
	# Make sure the post belongs to the user.
	if post.owner != request.user:
		raise Http404
	
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

@login_required
def delete_post(request, post_id):
	"""This is for deleting a selected post."""
	post = BlogPost.objects.get(id=post_id)
	if post.owner != request.user:
		raise Http404
	post.delete()
	return HttpResponseRedirect(reverse('weblogs:my_posts'))
	posts = BlogPost.objects.order_by('-date_added')
	context = {'posts': posts}
	return render(request, 'weblogs/my_posts.html', context)
	
