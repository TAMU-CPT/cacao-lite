# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-22 09:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_auto_20160722_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='challenge',
            old_name='uuid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='gaf',
            old_name='uuid',
            new_name='id',
        ),
    ]