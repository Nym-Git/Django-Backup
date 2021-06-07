# Generated by Django 3.1.7 on 2021-05-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoAPP', '0025_remove_instruction_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Complete', models.BooleanField(default=False)),
                ('Text_M', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Instruction',
        ),
    ]