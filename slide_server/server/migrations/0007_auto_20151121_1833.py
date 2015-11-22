# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20151121_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='VKAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('vk_group_id', models.CharField(max_length=20)),
                ('vk_album_id', models.CharField(max_length=20)),
                ('preview_img_URL', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VKImageCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('previewImgURL', models.CharField(max_length=150)),
                ('count_views', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='vkalbum',
            name='category',
            field=models.ForeignKey(to='server.VKImageCategory'),
        ),
    ]
