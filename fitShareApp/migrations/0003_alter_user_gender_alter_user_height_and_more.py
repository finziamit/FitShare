# Generated by Django 4.2.2 on 2023-08-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitShareApp', '0002_training_program_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.CharField(max_length=100),
        ),
    ]