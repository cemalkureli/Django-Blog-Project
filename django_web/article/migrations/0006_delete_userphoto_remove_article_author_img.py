# Generated by Django 4.1.3 on 2022-12-16 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_author_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserPhoto',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author_img',
        ),
    ]
