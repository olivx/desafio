# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_company_address'),
        ('core', '0006_auto_20170924_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='company',
            field=models.OneToOneField(null=True, blank=True, to='company.Company'),
        ),
    ]
