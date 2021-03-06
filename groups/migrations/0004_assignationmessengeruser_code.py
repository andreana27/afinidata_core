# Generated by Django 2.2.10 on 2020-03-04 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_rolegroupuser_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('available', models.BooleanField(default=True)),
                ('exchanges', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
        migrations.CreateModel(
            name='AssignationMessengerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messenger_user_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('code_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.Code')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.Group')),
            ],
        ),
    ]
