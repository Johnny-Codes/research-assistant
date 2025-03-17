from django.urls import path
from . import views

urlpatterns = [
    # path("projects/<int:project_id>/", views., name="article_detail"),
    path("", views.project_list_view, name="project_list"),
    path(
        "<int:project_id>/articles/",
        views.project_article_list_view,
        name="project_article_list",
    ),
]
