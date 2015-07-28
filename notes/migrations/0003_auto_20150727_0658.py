# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20150727_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created',
        ),
        migrations.RemoveField(
            model_name='note',
            name='done',
        ),
        migrations.RemoveField(
            model_name='note',
            name='due',
        ),
        migrations.RemoveField(
            model_name='note',
            name='updated',
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
