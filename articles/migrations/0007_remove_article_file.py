# Generated by Django 5.1.6 on 2025-03-21 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='file',
        ),
    ]
