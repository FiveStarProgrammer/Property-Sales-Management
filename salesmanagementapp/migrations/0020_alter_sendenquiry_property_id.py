# Generated by Django 4.2.7 on 2024-02-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagementapp', '0019_alter_sendenquiry_buy_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendenquiry',
            name='property_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
