# Generated by Django 3.1.7 on 2021-05-12 06:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='Likes_M',
            field=models.ManyToManyField(related_name='blog_Post', to=settings.AUTH_USER_MODEL),
        ),
    ]
