# Generated by Django 2.2.13 on 2020-08-11 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0008_auto_20200803_0905'),
        ('user_sessions', '0006_auto_20200810_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='programs.Level'),
        ),
    ]
