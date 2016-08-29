# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0002_auto_20160822_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='city',
        ),
        migrations.AddField(
            model_name='supplier',
            name='city_place_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.City_Place', null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='country_id',
            field=models.ForeignKey(blank=True, to='digispaceapp.Country', null=True),
        ),
    ]
