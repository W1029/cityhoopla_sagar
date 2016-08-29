# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0006_auto_20160827_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceratecard',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='serviceratecard',
            name='duration',
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.Category', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_level_1',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel1', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_level_2',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel2', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_level_3',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel3', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_level_4',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel4', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='category_level_5',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel5', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='city_place_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.City_Place', null=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='flag',
            field=models.CharField(default=None, max_length=15, null=True, blank=True, choices=[(b'1', b'1'), (b'0', b'0')]),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='ninty_days_cost',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='one_eighty_days_cost',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='seven_days_cost',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='thirty_days_cost',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='serviceratecard',
            name='three_days_cost',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
