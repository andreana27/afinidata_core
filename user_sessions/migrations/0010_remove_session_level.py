# Generated by Django 2.2.13 on 2020-08-12 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0009_auto_20200811_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='level',
        ),
    ]
