# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_multiplechoicequestion_truefalsequestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='content',
            new_name='total_questions',
        ),
    ]
