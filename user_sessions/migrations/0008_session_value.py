# Generated by Django 2.2.13 on 2020-08-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_sessions', '0007_session_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]