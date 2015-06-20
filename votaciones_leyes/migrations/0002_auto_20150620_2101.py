# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votaciones_leyes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='topic',
        ),
        migrations.AlterField(
            model_name='motion',
            name='proposal_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='role',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='voteevent',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
