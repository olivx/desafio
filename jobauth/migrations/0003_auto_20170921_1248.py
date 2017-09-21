# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobauth', '0002_auto_20170921_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='kind',
            field=models.PositiveIntegerField(default=2, verbose_name=b'Tipo', choices=[(1, b'Empresa'), (2, b'Candidato')]),
        ),
    ]
