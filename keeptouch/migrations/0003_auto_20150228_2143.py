# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keeptouch', '0002_auto_20150228_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'date published')),
                ('is_read', models.BooleanField(default=False)),
                ('user1', models.ForeignKey(related_name='user1', to='keeptouch.User')),
                ('user2', models.ForeignKey(related_name='user2', to='keeptouch.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(related_name='conversation', default=0, to='keeptouch.Conversation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
