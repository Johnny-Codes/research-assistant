# Generated by Django 5.1.6 on 2025-03-21 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_article_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
