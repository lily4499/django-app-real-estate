# Generated by Django 3.2 on 2024-12-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_property_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='indian_currency',
            field=models.CharField(default='INR', max_length=30),
        ),
    ]
