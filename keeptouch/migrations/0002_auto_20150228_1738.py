# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.ForeignKey(related_name='reciever', to='keeptouch.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(related_name='sender', to='keeptouch.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='thumbnail',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
