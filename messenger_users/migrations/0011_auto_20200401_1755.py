# Generated by Django 2.2.10 on 2020-04-01 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger_users', '0010_useractivity_useractivitylog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('view_all_messenger_users', 'Platform User can view all Messenger Users.'),)},
        ),
    ]
