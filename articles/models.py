from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        "Tag",
        related_name="articles",
    )
    project = models.ManyToManyField(
        "Project",
        related_name="articles",
        blank=True,
    )
    summary = models.TextField(blank=True, null=True)
    file = models.FileField(
        upload_to="uploads/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
