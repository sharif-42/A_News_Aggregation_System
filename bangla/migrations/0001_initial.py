# Generated by Django 2.2 on 2019-12-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BanglaNews',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('news_paper_name', models.CharField(max_length=100)),
                ('headline', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('news_category', models.CharField(choices=[('MR', 'Most read'), ('BN', 'Breaking news'), ('NA', 'National'), ('IN', 'Inter national'), ('PL', 'Politics'), ('SP', 'Sports'), ('EN', 'Entertainment'), ('TN', 'Technology')], default='MR', max_length=2)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'News Paper',
                'verbose_name_plural': 'News Papers',
            },
        ),
        migrations.AddIndex(
            model_name='banglanews',
            index=models.Index(fields=['id', 'news_category', 'news_paper_name', 'publish_time'], name='bangla_bang_id_fa60fd_idx'),
        ),
    ]
