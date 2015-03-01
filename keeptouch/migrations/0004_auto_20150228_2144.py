# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0003_auto_20150228_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(related_name='conversation', default=1, to='keeptouch.Conversation'),
            preserve_default=True,
        ),
    ]
