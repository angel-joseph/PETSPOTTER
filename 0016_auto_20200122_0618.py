# Generated by Django 2.2.5 on 2020-01-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20200122_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_food',
            name='rating',
            field=models.FloatField(default=0, max_length=30),
        ),
        migrations.AddField(
            model_name='add_pets',
            name='rating',
            field=models.FloatField(default=0, max_length=30),
        ),
    ]
