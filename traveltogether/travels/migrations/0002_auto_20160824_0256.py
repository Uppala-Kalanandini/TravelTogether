# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 23:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='owner',
            new_name='creator',
        ),
    ]
