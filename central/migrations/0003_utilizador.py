# Generated by Django 4.1.4 on 2022-12-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_jogadortest_delete_alunotest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=8)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
    ]
