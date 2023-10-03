# Generated by Django 4.2.5 on 2023-10-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_alter_chapter_options_remove_chapter_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='count_like',
        ),
        migrations.RemoveField(
            model_name='title',
            name='count_view',
        ),
        migrations.AddField(
            model_name='chapter',
            name='count_like',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='chapter',
            name='count_view',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]