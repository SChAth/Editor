# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xml_edit_forms', '0003_auto_20170211_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmleditform',
            name='file_type',
            field=models.CharField(choices=[('<property object at 0x7f1b5e13aef8>', '<property object at 0x7f1b5e13aef8>'), ('<property object at 0x7f1b5e13aef8>', '<property object at 0x7f1b5e13aef8>'), ('<property object at 0x7f1b5e13aef8>', '<property object at 0x7f1b5e13aef8>'), ('<property object at 0x7f1b5e13aef8>', '<property object at 0x7f1b5e13aef8>')], max_length=100),
        ),
    ]
