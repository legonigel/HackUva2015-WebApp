# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0006_auto_20150228_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='last_message',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
