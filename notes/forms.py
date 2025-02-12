from django import forms
from .models import ArticleQuestion

class AnswerForm(forms.ModelForm):
	class Meta:
		model = ArticleQuestion
		fields = ['answer']
