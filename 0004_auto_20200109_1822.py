# Generated by Django 2.2.5 on 2020-01-09 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200109_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_tb',
            name='fid',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_food'),
        ),
    ]
