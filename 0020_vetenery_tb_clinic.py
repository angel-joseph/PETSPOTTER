# Generated by Django 2.2.5 on 2020-02-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20200213_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetenery_tb',
            name='clinic',
            field=models.CharField(default='', max_length=100),
        ),
    ]
