# Generated by Django 3.1.7 on 2021-05-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAPP', '0020_remove_instruction_user_name_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='Complete',
            field=models.BooleanField(),
        ),
    ]