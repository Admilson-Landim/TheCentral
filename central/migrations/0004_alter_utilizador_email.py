# Generated by Django 4.1.4 on 2022-12-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_utilizador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilizador',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]