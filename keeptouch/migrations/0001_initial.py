# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=500)),
                ('expiration', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_read', models.BooleanField()),
                ('timestamp', models.DateTimeField(verbose_name=b'date published')),
                ('message_text', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(upload_to=b'')),
                ('fb_id', models.CharField(max_length=100)),
                ('is_online', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='reciever',
            field=models.OneToOneField(related_name='reciever', to='keeptouch.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.OneToOneField(related_name='sender', to='keeptouch.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='connection',
            name='user',
            field=models.ForeignKey(to='keeptouch.User'),
            preserve_default=True,
        ),
    ]
