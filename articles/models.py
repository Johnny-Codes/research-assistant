from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=256)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField("Tag", related_name="articles")
	def __str__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=256)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Tag(models.Model):
	text = models.CharField(max_length=256)

	def __str__(self):
		return self.text
