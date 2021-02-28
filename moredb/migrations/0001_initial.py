# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=20, verbose_name='\u56fe\u4e66\u540d')),
                ('bpub_date', models.DateField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('bread', models.IntegerField(default=0, verbose_name='\u9605\u8bfb\u91cf')),
                ('bcomment', models.IntegerField(default=0, verbose_name='\u8bc4\u8bba\u91cf')),
                ('is_delete', models.BooleanField(default=False, verbose_name='\u903b\u8f91\u5220\u9664')),
            ],
            options={
                'verbose_name': '\u56fe\u4e66\u4fe1\u606f',
            },
        ),
    ]
