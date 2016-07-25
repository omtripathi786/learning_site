# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True, default='')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.RemoveField(
            model_name='step',
            name='course',
        ),
        migrations.DeleteModel(
            name='Step',
        ),
    ]
