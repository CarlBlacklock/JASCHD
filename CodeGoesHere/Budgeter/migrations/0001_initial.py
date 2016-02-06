# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateField()),
                ('transaction_type', models.TextField()),
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
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('user_bank_name', models.TextField()),
            ],
        ),
    ]