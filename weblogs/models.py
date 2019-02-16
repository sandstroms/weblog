from django.db import models

class BlogPost(models.Model):
	"""A post for any site visitors to see."""
	title = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	body = models.TextField()
	
	def __str__(self):
		"""Return a string representation of the model."""
		return self.title
