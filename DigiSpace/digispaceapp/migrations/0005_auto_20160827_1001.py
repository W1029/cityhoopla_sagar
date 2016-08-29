# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0004_auto_20160825_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertratecard',
            name='ninty_days',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='one_eighty_days',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='seven_days',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='thirty_days',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='three_days',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='advertratecard',
            name='advert_service_name',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='advertratecard',
            name='flag',
            field=models.CharField(default=None, max_length=15, null=True, blank=True, choices=[(b'1', b'1'), (b'0', b'0')]),
        ),
    ]
