# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 08:14
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_auto_20170223_0809'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('UserManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
