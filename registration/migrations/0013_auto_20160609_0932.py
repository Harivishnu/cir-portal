# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20160609_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='tenth_mark',
            field=models.FloatField(max_length=5, null=True, verbose_name='10th Mark', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='twelth_mark',
            field=models.FloatField(max_length=5, null=True, verbose_name='12th Mark', blank=True),
        ),
    ]
