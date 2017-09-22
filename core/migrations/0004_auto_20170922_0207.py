# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170921_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Vaga')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('salario_min', models.DecimalField(verbose_name=b'Salario Minimo', max_digits=10, decimal_places=2)),
                ('salario_max', models.DecimalField(verbose_name=b'Salario Max', max_digits=10, decimal_places=2)),
                ('experiencia', models.PositiveIntegerField(default=1, verbose_name=b'Experiencia', choices=[(1, b'6 Meses'), (2, b'1 ano'), (2, b'2 anos '), (3, b'3 anos '), (4, b'4 anos '), (5, b'5 anos ou mais ')])),
                ('escolaridade', models.PositiveIntegerField(default=1, verbose_name=b'Escolaridade', choices=[(1, b'Ensino superior completo'), (2, b'Ensino superior cursando'), (3, b'Nivel Tecnico'), (4, b'Segundo Grau completo '), (5, b'Segundo Grau cursando')])),
                ('distancia_max', models.IntegerField(verbose_name=b'Distancia Maxima')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='escolariodade',
            new_name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='company',
            name='distancia_max',
        ),
        migrations.RemoveField(
            model_name='company',
            name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='company',
            name='experiencia',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salario_max',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salario_min',
        ),
        migrations.RemoveField(
            model_name='company',
            name='vaga',
        ),
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default=datetime.datetime(2017, 9, 22, 2, 7, 52, 41846, tzinfo=utc), max_length=100, verbose_name=b'Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(to='core.Company'),
        ),
    ]
