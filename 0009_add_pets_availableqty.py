# Generated by Django 2.2.5 on 2020-01-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_add_pets_availableqty'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_pets',
            name='availableqty',
            field=models.CharField(default='', max_length=30),
        ),
    ]
