# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sku',
            name='order_number',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
