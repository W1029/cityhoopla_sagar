# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0003_auto_20160823_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertratecard',
            name='category_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.Category', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='category_level_1',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel1', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='category_level_2',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel2', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='category_level_3',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel3', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='category_level_4',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel4', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='category_level_5',
            field=models.ForeignKey(blank=True, to='digispaceapp.CategoryLevel5', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='city_place_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.City_Place', null=True),
        ),
        migrations.AddField(
            model_name='advertratecard',
            name='flag',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
