from django.db import models
from django.conf import settings

import semchunk
import pymupdf4llm
import tiktoken

import weaviate

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
    embedding_id = models.CharField(max_length=36, blank=True, null=True,)
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
        try:
            client = weaviate.connect_to_local()
            print("Successfully connected to weaviate")
        except Exception as e:
            print(f"error connecting to weaviate {e}")
            client = None

        with client.batch as batch:
            batch.batch_size = 10
            embedding_ids = []
            for chunk in chunks:
                response = batch.add_data_objects(
                    data_object={"content": chunk},
                    class_name="ResearchArticle"
                )
                embedding_id = response['id']
                embedding_ids.append(embedding_id)
            self.embedding_id = ','.join(embedding_ids)
            self.save()
        

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
