# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': "Item's",
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='MenuPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exile.Menu')),
            ],
            options={
                'verbose_name': 'Menu principal',
                'verbose_name_plural': 'Menu principal',
            },
        ),
        migrations.CreateModel(
            name='OrdenItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Item')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Menu')),
            ],
            options={
                'verbose_name': 'Orden de item',
                'verbose_name_plural': 'Orden de items',
            },
        ),
        migrations.CreateModel(
            name='OrdenSubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Item')),
            ],
            options={
                'verbose_name': 'Orden de subitem',
                'verbose_name_plural': 'Ordenes de subitem',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
                ('contenido', models.TextField()),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Page')),
            ],
            options={
                'verbose_name': 'Secci\xf3n',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Page')),
            ],
            options={
                'verbose_name': 'SubItem',
                'verbose_name_plural': "SubItem's",
            },
        ),
        migrations.AddField(
            model_name='ordensubitem',
            name='subitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.SubItem'),
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(through='exile.OrdenItem', to='exile.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='principal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exile.Page', verbose_name='Pagina Principal'),
        ),
        migrations.AddField(
            model_name='item',
            name='subitems',
            field=models.ManyToManyField(through='exile.OrdenSubItem', to='exile.SubItem'),
        ),
    ]