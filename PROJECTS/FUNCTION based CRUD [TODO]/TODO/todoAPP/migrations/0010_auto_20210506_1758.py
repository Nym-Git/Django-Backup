# Generated by Django 3.1.7 on 2021-05-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAPP', '0009_auto_20210506_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='Complete',
            field=models.BooleanField(),
        ),
    ]
