# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-11 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exile', '0006_seccion_posicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=300)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FooterPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('footer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exile.Footer')),
            ],
            options={
                'verbose_name': 'Footer Principal',
                'verbose_name_plural': 'Footer Principal',
            },
        ),
        migrations.CreateModel(
            name='OrdenFooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Footer')),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.Page')),
            ],
        ),
        migrations.CreateModel(
            name='SeccionFooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='ordenfooter',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exile.SeccionFooter'),
        ),
        migrations.AddField(
            model_name='footer',
            name='paginas',
            field=models.ManyToManyField(through='exile.OrdenFooter', to='exile.Page'),
        ),
    ]
