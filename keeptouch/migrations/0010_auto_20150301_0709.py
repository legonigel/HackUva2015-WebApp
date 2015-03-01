# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0009_auto_20150301_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='user1_name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conversation',
            name='user2_name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
