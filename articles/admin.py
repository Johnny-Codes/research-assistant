from django.contrib import admin
from .models import Article, Tag, Project
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    fields = ("title", "user", "created_at", "tags", "project", "summary", "file")
    readonly_fields = ("created_at",)
admin.site.register(Tag)
admin.site.register(Project)
