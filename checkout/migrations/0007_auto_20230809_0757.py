# Generated by Django 3.2.20 on 2023-08-09 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_street_address2_order_street_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address1',
        ),
    ]