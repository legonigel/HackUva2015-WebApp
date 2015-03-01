# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0011_auto_20150301_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='thumbnail',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
