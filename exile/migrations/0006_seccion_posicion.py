# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exile', '0005_auto_20160915_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='seccion',
            name='posicion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
