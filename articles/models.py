from django.db import models
from django.conf import settings

import semchunk
import pymupdf4llm
import tiktoken

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
    file = models.FileField(upload_to="uploads/", blank=True, null=True,)
    chunked = models.BooleanField(default=False)

    def chunk_article(self):
        if self.chunked == True:
            return f'{self.title} has already been chunked'
        # step 1: turn to markdown
        md_text = pymupdf4llm.to_markdown(f'{settings.MEDIA_ROOT}/{self.file}') 
        # step 2: chunk with semchunk and tiktoken
        chunk_size=500
        chunker = semchunk.chunkerify(tiktoken.encoding_for_model('gpt-4'), chunk_size)
        chunks = chunker(md_text)
        # step 3: embed
        self.chunked = True
        

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
