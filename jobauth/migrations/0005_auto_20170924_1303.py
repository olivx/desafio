# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobauth', '0004_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='last_job',
            field=models.TextField(null=True, verbose_name=b'Ultimo Emprego', blank=True),
        ),
    ]
