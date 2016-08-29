# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0005_auto_20160827_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertratecard',
            old_name='ninty_days',
            new_name='ninty_days_cost',
        ),
        migrations.RenameField(
            model_name='advertratecard',
            old_name='one_eighty_days',
            new_name='one_eighty_days_cost',
        ),
        migrations.RenameField(
            model_name='advertratecard',
            old_name='seven_days',
            new_name='seven_days_cost',
        ),
        migrations.RenameField(
            model_name='advertratecard',
            old_name='thirty_days',
            new_name='thirty_days_cost',
        ),
        migrations.RenameField(
            model_name='advertratecard',
            old_name='three_days',
            new_name='three_days_cost',
        ),
        migrations.RemoveField(
            model_name='advertratecard',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='advertratecard',
            name='duration',
        ),
    ]
