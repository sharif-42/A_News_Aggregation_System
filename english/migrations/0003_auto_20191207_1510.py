# Generated by Django 2.2 on 2019-12-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0002_auto_20191207_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News Paper', 'verbose_name_plural': 'News Papers'},
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['id', 'news_category', 'news_paper_name', 'publish_time'], name='english_new_id_91c2c7_idx'),
        ),
    ]
