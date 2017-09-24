# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_address_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='user',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
    ]
