# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Initiated'), (1, b'Completed')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(unique=True, max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=10, null=True, blank=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Active'), (1, b'InActive')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ean_code', models.CharField(unique=True, max_length=13)),
                ('description', models.CharField(max_length=50, null=True, blank=True)),
                ('brand', models.CharField(max_length=100, null=True, blank=True)),
                ('category', models.CharField(max_length=100, null=True, blank=True)),
                ('colour', models.CharField(max_length=100, null=True, blank=True)),
                ('size', models.CharField(max_length=100, null=True, blank=True)),
                ('mrp', models.CharField(default=0, max_length=100)),
                ('length', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='customer',
            field=models.ForeignKey(to='cart_app.Customer'),
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='sku',
            field=models.ManyToManyField(to='cart_app.SKU'),
        ),
    ]
