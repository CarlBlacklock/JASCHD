# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgeter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='merchant_name',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
