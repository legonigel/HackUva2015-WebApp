# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0004_auto_20150228_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(related_name='conversation', default=b'1', to='keeptouch.Conversation'),
            preserve_default=True,
        ),
    ]
