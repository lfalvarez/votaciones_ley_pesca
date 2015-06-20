# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popolo', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legislative_session', models.CharField(max_length=512, null=True)),
                ('text', models.TextField()),
                ('proposal_date', models.DateField()),
                ('requirement', models.TextField()),
                ('result', models.CharField(max_length=512)),
                ('creator', models.ForeignKey(to='popolo.Person', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoDeLey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boletin', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.TextField()),
                ('option', models.CharField(max_length=512, choices=[(b'yes', b'Yes'), (b'no', b'No'), (b'abstain', b'Abstain'), (b'absent', b'Absent'), (b'not_voting', b'Not voting'), (b'paired', b'Paired')])),
                ('role', models.CharField(max_length=512)),
                ('political_group', models.ForeignKey(to='popolo.Organization', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VoteEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('legislative_session', models.CharField(max_length=512, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('motion', models.ForeignKey(related_name='vote_events', to='votaciones_leyes.Motion', null=True)),
                ('organization', models.ForeignKey(to='popolo.Organization', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_event',
            field=models.ForeignKey(to='votaciones_leyes.VoteEvent', null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(to='popolo.Person', null=True),
        ),
        migrations.AddField(
            model_name='motion',
            name='proyecto_de_ley',
            field=models.ForeignKey(to='votaciones_leyes.ProyectoDeLey', null=True),
        ),
    ]
