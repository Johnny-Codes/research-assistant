from django.shortcuts import render, get_object_or_404
from .models import Project, Article, Tag


def project_list_view(request):
    projects = Project.objects.all()
    return render(request, "./articles/project_list.html", {"projects": projects})


def project_article_list_view(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    articles = Article.objects.filter(project=project_id)
    return render(
        request,
        "./articles/article_list.html",
        {"project": project, "articles": articles},
    )
