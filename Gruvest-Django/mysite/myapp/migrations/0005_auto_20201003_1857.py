# Generated by Django 3.1.1 on 2020-10-03 18:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_auto_20201002_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='DownVote',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='DownVote',
            field=models.ManyToManyField(related_name='pitchDown', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='UpVote',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='UpVote',
            field=models.ManyToManyField(related_name='pitchUp', to=settings.AUTH_USER_MODEL),
        ),
    ]
