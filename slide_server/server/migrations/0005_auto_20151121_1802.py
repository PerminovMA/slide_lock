# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20151121_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='error',
            old_name='functionName',
            new_name='function_name',
        ),
    ]
