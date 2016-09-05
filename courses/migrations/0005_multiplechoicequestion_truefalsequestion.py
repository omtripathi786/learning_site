# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20160726_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(to='courses.Question', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('shuffle_answers', models.BooleanField(default=False)),
            ],
            bases=('courses.question',),
        ),
        migrations.CreateModel(
            name='TrueFalseQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(to='courses.Question', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
            ],
            bases=('courses.question',),
        ),
    ]
