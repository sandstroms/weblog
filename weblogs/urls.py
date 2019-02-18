"""Defines URL patterns for weblogs."""

from django.urls import path

from . import views

app_name = 'weblogs'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	
	# Page for adding a new post
	path('new_post/', views.new_post, name='new_post'),
	
	# Page for viewing posts
	path('my_posts/', views.my_posts, name='my_posts'),
	
	# Page for editing posts
	path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
	
	# For deleting a post.
	path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
