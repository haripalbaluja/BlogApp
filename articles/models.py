from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=100)
	slug  = models.SlugField()
	body  = models.TextField()
	date  = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.png", blank=True) 
	author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

	# add in thumbnail
	# add in author later

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + '...'	


class Comment(models.Model):
    post = models.ForeignKey('articles.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text	





