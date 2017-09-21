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
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logradouro', models.CharField(max_length=50, verbose_name=b'Logradouro')),
                ('endereco', models.CharField(max_length=60, verbose_name=b'Endereco')),
                ('numero', models.PositiveIntegerField(verbose_name=b'Numero')),
                ('complemento', models.CharField(max_length=40, null=True, verbose_name=b'Complemento', blank=True)),
                ('cep', models.CharField(max_length=11, verbose_name=b'Cep')),
                ('bairro', models.CharField(max_length=100, verbose_name=b'Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name=b'Cidade')),
                ('uf', models.CharField(max_length=20, verbose_name=b'UF')),
                ('observacao', models.TextField(null=True, blank=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salario', models.DecimalField(verbose_name=b'Salario Pretenido', max_digits=10, decimal_places=2)),
                ('experiencia', models.PositiveIntegerField(default=1, verbose_name=b'Experiencia', choices=[(1, b'6 Meses'), (2, b'1 ano'), (2, b'2 anos '), (3, b'3 anos '), (4, b'4 anos '), (5, b'5 anos ou mais ')])),
                ('escolariodade', models.PositiveIntegerField(default=1, verbose_name=b'Escolaridade', choices=[(1, b'Ensino superior completo'), (2, b'Ensino superior cursando'), (3, b'Nivel Tecnico'), (4, b'Segundo Grau completo '), (5, b'Segundo Grau cursando')])),
                ('end', models.ForeignKey(to='core.Address')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vaga', models.CharField(max_length=100, verbose_name=b'Vaga')),
                ('salario_min', models.DecimalField(verbose_name=b'Salario Minimo', max_digits=10, decimal_places=2)),
                ('salario_max', models.DecimalField(verbose_name=b'Salario Max', max_digits=10, decimal_places=2)),
                ('experiencia', models.PositiveIntegerField(default=1, verbose_name=b'Experiencia', choices=[(1, b'6 Meses'), (2, b'1 ano'), (2, b'2 anos '), (3, b'3 anos '), (4, b'4 anos '), (5, b'5 anos ou mais ')])),
                ('escolariodade', models.PositiveIntegerField(default=1, verbose_name=b'Escolaridade', choices=[(1, b'Ensino superior completo'), (2, b'Ensino superior cursando'), (3, b'Nivel Tecnico'), (4, b'Segundo Grau completo '), (5, b'Segundo Grau cursando')])),
                ('distancia_max', models.IntegerField(verbose_name=b'Distancia Maxima')),
                ('end', models.ForeignKey(blank=True, to='core.Address', null=True)),
            ],
            options={
                'verbose_name': 'Endereco',
                'verbose_name_plural': 'Enderecos',
            },
        ),
    ]
