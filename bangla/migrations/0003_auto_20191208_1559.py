# Generated by Django 2.2 on 2019-12-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0002_auto_20191207_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banglanews',
            name='news_category',
            field=models.CharField(choices=[('Most read', 'Most read'), ('Breaking news', 'Breaking news'), ('National', 'National'), ('Inter National', 'Inter National'), ('Politics', 'Politics'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology')], default='Most read', max_length=20),
        ),
    ]
