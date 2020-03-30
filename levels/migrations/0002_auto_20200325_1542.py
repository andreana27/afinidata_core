# Generated by Django 2.2.10 on 2020-03-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='level',
            name='max',
        ),
        migrations.RemoveField(
            model_name='level',
            name='min',
        ),
        migrations.RemoveField(
            model_name='level',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='level',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='range_max',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='range_min',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]