# Generated by Django 4.1.3 on 2022-12-16 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_options_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
