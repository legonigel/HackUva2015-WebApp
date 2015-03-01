# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0010_auto_20150301_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='last_message',
            field=models.CharField(max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
