# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170921_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='end',
        ),
        migrations.RemoveField(
            model_name='company',
            name='end',
        ),
        migrations.AddField(
            model_name='address',
            name='end',
            field=models.ForeignKey(blank=True, to='core.Candidate', null=True),
        ),
    ]
