# Generated by Django 3.2.5 on 2021-07-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210726_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='Status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]