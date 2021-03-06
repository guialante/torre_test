# Generated by Django 2.0.4 on 2018-04-15 21:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='extra_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='Extra Data'),
        ),
        migrations.AddField(
            model_name='user',
            name='headline',
            field=models.CharField(default='', max_length=160, verbose_name='Headline'),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='', max_length=120, verbose_name='Location'),
        ),
        migrations.AddField(
            model_name='user',
            name='summary',
            field=models.TextField(blank=True, default='', verbose_name='Summary of your bio (optional)'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Name of User'),
        ),
    ]
