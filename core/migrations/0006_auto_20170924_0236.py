# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170922_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company',
        ),
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name': 'Candidatos', 'verbose_name_plural': 'Candidatos'},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='escolaridade',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Escolaridade', choices=[(0, b'-------------'), (1, b'Ensino superior completo'), (2, b'Ensino superior cursando'), (3, b'Nivel Tecnico'), (4, b'Segundo Grau completo '), (5, b'Segundo Grau cursando')]),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='experiencia',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Experiencia', choices=[(1, b'6 Meses'), (2, b'1 ano'), (2, b'2 anos '), (3, b'3 anos '), (4, b'4 anos '), (5, b'5 anos ou mais ')]),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
