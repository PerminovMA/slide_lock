# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20151121_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')]),
        ),
    ]
