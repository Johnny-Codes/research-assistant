from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article, QuestionBank, ArticleQuestion

@receiver(post_save, sender=Article)
def create_article_question(sender, instance, created, **kwargs):
	if created:
		# Create a new ArticleQuestion instance for the newly created Article
		questions = QuestionBank.objects.all()

		for question in questions:
			ArticleQuestion.objects.create(article=instance, question=question)

@receiver(post_save, sender=QuestionBank)
def add_new_question_to_all_articles(sender, instance, created, **kwargs):
	if created:
		# Add the new question to all existing articles
		articles = Article.objects.all()

		for article in articles:
			ArticleQuestion.objects.create(article=article, question=instance)
