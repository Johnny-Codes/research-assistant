from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(QuestionBank)
admin.site.register(ArticleQuestion)
