# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exile', '0003_auto_20160914_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaginaPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Page')),
            ],
            options={
                'verbose_name': 'Pagina principal',
                'verbose_name_plural': 'Pagina principal',
            },
        ),
    ]
