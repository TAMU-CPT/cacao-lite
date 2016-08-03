# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_auto_20160802_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='gaf',
        ),
        migrations.AddField(
            model_name='challenge',
            name='challenge_gaf',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='challenge_gaf', to='base.GAF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='challenge',
            name='original_gaf',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='original_gaf', to='base.GAF'),
            preserve_default=False,
        ),
    ]
