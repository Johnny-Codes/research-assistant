from django.urls import path
from . import views

urlpatterns = [
    path("article/<int:article_id>/", views.article_detail, name="article_detail"),
    path("articles/", views.article_list, name="article_list"),
]
