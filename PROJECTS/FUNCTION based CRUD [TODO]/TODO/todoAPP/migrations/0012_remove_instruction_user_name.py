# Generated by Django 3.1.7 on 2021-05-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoAPP', '0011_auto_20210506_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='User_name',
        ),
    ]