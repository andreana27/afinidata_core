# Generated by Django 2.2.10 on 2020-03-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_users', '0005_auto_20200304_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_channel_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
