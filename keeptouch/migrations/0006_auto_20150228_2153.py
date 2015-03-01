# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0005_auto_20150228_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='timestamp',
            field=models.DateTimeField(verbose_name=b'last published'),
            preserve_default=True,
        ),
    ]
