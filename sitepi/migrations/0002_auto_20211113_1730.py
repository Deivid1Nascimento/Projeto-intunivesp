# Generated by Django 3.2.9 on 2021-11-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitepi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculdades',
            name='modificado',
        ),
        migrations.AlterField(
            model_name='faculdades',
            name='descricao',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='faculdades',
            name='modalidade',
            field=models.CharField(max_length=20),
        ),
    ]
