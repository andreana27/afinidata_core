# Generated by Django 2.2.10 on 2020-04-03 22:52

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0003_auto_20200329_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='levels',
        ),
        migrations.AddField(
            model_name='area',
            name='backgroundColor',
            field=colorfield.fields.ColorField(blank=True, default='#ff0000', max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='area',
            name='pointColor',
            field=colorfield.fields.ColorField(blank=True, default='#ff0000', max_length=18, null=True),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
