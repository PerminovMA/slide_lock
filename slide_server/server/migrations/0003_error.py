# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20151121_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('explanation', models.CharField(max_length=100, null=True, blank=True)),
                ('errorid', models.CharField(max_length=10, null=True, blank=True)),
                ('functionName', models.CharField(max_length=100, null=True, blank=True)),
                ('errorDateTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
