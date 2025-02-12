from django.db import models
from django.conf import settings

class Article(models.Model):
	title = models.CharField(max_length=256)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class QuestionBank(models.Model):
	text = models.CharField(max_length=256)

	def __str__(self):
		return self.text

class ArticleQuestion(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="questions")
	question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, related_name = "articles")
	answer = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.article.title} - {self.question.text}"
