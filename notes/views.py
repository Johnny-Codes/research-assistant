from django.shortcuts import (render, redirect, get_object_or_404,)
from django.http import HttpResponse
from .models import *
from .forms import *
from articles.models import Article


def article_detail(request, article_id):
	article_questions = ArticleQuestion.objects.filter(article=article_id)

	if request.method == 'POST':
		for data in article_questions:
			answer = request.POST.get(f'answer_{data.id}')
			if answer:
				data.answer = answer
				data.save()
		return redirect('article_detail', article_id=article_id)
	return render(request, './notes/article_detail.html', {'article_questions': article_questions})

def article_list(request):
	articles = Article.objects.all()
	return render(request, './notes/article_list.html', {'articles': articles})
