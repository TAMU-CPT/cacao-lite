# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refseq',
            name='length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='refseq',
            name='name',
            field=models.CharField(default='adsf', max_length=64),
            preserve_default=False,
        ),
    ]
