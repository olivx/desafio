# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Empresa')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Vaga')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('salario_min', models.DecimalField(verbose_name=b'Salario Minimo', max_digits=10, decimal_places=2)),
                ('salario_max', models.DecimalField(verbose_name=b'Salario Max', max_digits=10, decimal_places=2)),
                ('experiencia', models.PositiveIntegerField(default=0, verbose_name=b'Experiencia', choices=[(1, b'6 Meses'), (2, b'1 ano'), (2, b'2 anos '), (3, b'3 anos '), (4, b'4 anos '), (5, b'5 anos ou mais ')])),
                ('escolaridade', models.PositiveIntegerField(default=0, verbose_name=b'Escolaridade', choices=[(0, b'-------------'), (1, b'Ensino superior completo'), (2, b'Ensino superior cursando'), (3, b'Nivel Tecnico'), (4, b'Segundo Grau completo '), (5, b'Segundo Grau cursando')])),
                ('distancia_max', models.IntegerField(verbose_name=b'D. Maxima')),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
