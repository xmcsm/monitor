# Generated by Django 2.2.12 on 2020-05-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('host_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('configuration', models.TextField()),
                ('status', models.CharField(max_length=12)),
                ('message', models.TextField()),
                ('enable', models.IntegerField(default=1)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'app',
            },
        ),
        migrations.CreateModel(
            name='AppHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('status', models.CharField(max_length=32)),
                ('message', models.TextField(null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'app_history',
            },
        ),
        migrations.CreateModel(
            name='AppStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField()),
                ('statistics', models.CharField(max_length=256)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'app_statistics',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_name', models.CharField(max_length=32)),
                ('display_name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'app_group',
            },
        ),
    ]
