# Generated by Django 2.2.5 on 2020-01-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_review_tb_cartid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_food',
            name='rating',
            field=models.IntegerField(default=0, max_length=30),
        ),
        migrations.AlterField(
            model_name='add_pets',
            name='rating',
            field=models.IntegerField(default=0, max_length=30),
        ),
    ]
