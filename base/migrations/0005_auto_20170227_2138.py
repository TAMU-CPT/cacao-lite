# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-27 21:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20170227_2134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='refseq',
            unique_together=set([('name', 'organism')]),
        ),
    ]