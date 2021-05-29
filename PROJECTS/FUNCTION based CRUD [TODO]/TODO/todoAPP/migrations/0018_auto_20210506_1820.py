# Generated by Django 3.1.7 on 2021-05-06 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoAPP', '0017_auto_20210506_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='Complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='User_name',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
