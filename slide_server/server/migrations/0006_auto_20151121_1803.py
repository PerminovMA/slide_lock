# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20151121_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='error',
            old_name='errorDateTime',
            new_name='error_date_time',
        ),
    ]
