# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_address_company'),
        ('company', '0005_auto_20170925_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.OneToOneField(null=True, blank=True, to='core.Address'),
        ),
    ]
