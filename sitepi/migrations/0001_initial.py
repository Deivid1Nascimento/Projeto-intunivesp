# Generated by Django 3.2.9 on 2021-11-10 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculdades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_faculdade', models.CharField(max_length=30)),
                ('curso', models.CharField(max_length=20)),
                ('preco', models.FloatField()),
                ('descricao', models.CharField(max_length=50)),
                ('datacriacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('modificado', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('notaenade', models.FloatField(max_length=6)),
                ('nota', models.IntegerField()),
                ('cidade', models.CharField(max_length=20)),
                ('uf', models.CharField(max_length=2)),
                ('modalidade', models.CharField(max_length=50)),
            ],
        ),
    ]