# Generated by Django 2.2 on 2019-12-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0003_auto_20191208_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banglanews',
            name='news_category',
            field=models.CharField(choices=[('Most Read', 'Most Read'), ('Breaking News', 'Breaking News'), ('National', 'National'), ('Inter National', 'Inter National'), ('Politics', 'Politics'), ('Sports', 'Sports'), ('Entertainment', 'Entertainment'), ('Technology', 'Technology')], default='Most Read', max_length=20),
        ),
    ]
