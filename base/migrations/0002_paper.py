# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-08 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('author', models.TextField()),
                ('pub_year', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField()),
                ('journal', models.CharField(max_length=64)),
                ('volume', models.IntegerField()),
                ('pages', models.CharField(max_length=64)),
                ('abstract', models.TextField()),
                ('keywords', models.TextField()),
                ('pmc', models.IntegerField(null=True)),
            ],
        ),
    ]
