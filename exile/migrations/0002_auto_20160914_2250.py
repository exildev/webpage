# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='subitem',
            name='seccion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exile.ItemSeccion'),
            preserve_default=False,
        ),
    ]
