# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170922_0207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-id'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id'], 'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
        migrations.RemoveField(
            model_name='address',
            name='end',
        ),
        migrations.AddField(
            model_name='job',
            name='candidates',
            field=models.ManyToManyField(to='core.Candidate'),
        ),
        migrations.AlterField(
            model_name='job',
            name='distancia_max',
            field=models.IntegerField(verbose_name=b'D. Maxima'),
        ),
    ]
