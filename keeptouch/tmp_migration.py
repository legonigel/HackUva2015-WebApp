# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0002_auto_20150228_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(related_name='conversation', default=0, to='keeptouch.Conversation'),
            preserve_default=True,
        ),
    ]
