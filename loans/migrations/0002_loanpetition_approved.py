# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanpetition',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
