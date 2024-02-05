# Generated by Django 4.2.7 on 2024-02-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanagementapp', '0021_alter_sendenquiry_confirmation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoldProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=255, null=True)),
                ('property_name', models.CharField(max_length=255)),
                ('property_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Independent Floor', 'Independent Floor'), ('Builder Floor', 'Builder Floor'), ('Villa', 'Villa')], max_length=20)),
                ('status_name', models.CharField(choices=[('Ready to Move', 'Ready to Move'), ('Resale', 'Resale'), ('Under Construction', 'Under Construction')], max_length=20)),
                ('property_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_size', models.CharField(max_length=200)),
                ('seller_contact_details', models.BigIntegerField()),
                ('email_property', models.TextField(default='Default Amenities')),
                ('property_amenities', models.TextField(default='Default Amenities')),
                ('property_specifications', models.TextField(default='Default Amenities')),
                ('property_total_rooms', models.PositiveIntegerField()),
                ('property_balcony', models.CharField(max_length=200)),
                ('property_total_bathrooms', models.PositiveIntegerField()),
                ('property_address', models.TextField(default='Default Amenities')),
                ('property_image', models.ImageField(upload_to='uimg/')),
                ('property_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='sendenquiry',
            name='confirmation',
            field=models.CharField(choices=[('Purchased', 'Purchased'), ('Purchase Declined', 'Purchase Declined')], max_length=255, null=True),
        ),
    ]
