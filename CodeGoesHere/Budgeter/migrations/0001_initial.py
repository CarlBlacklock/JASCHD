# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 16:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bank_name', models.TextField()),
                ('user_id', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('merchant_name', models.TextField(default='Unknown')),
                ('transaction_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Budgeter.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionCatagories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.TextField()),
                ('merchant_catagory', models.TextField(choices=[('STAPLEFOOD', 'Staple Food'), ('ENTERTAINMENT', 'Entertainment'), ('ELECTRONICS', 'Electronics'), ('OTHERFOOD', 'Other Food'), ('CLOTHING', 'Clothing'), ('TRANSPORTATION', 'Transportation')])),
            ],
        ),
    ]
