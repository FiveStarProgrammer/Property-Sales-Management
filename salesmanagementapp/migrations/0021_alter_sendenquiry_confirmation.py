# Generated by Django 4.2.7 on 2024-02-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagementapp', '0020_alter_sendenquiry_property_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendenquiry',
            name='confirmation',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Declined', 'Declined')], max_length=255, null=True),
        ),
    ]
