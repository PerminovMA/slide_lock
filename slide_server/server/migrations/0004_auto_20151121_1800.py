# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_error'),
    ]

    operations = [
        migrations.RenameField(
            model_name='error',
            old_name='errorid',
            new_name='error_id',
        ),
    ]
