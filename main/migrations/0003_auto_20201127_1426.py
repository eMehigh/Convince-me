# Generated by Django 3.0.3 on 2020-11-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201109_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='creator_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='room',
            name='pair_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
