# Generated by Django 2.2.10 on 2020-03-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_language_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='languagecode',
            name='code',
            field=models.CharField(max_length=5),
        ),
    ]
