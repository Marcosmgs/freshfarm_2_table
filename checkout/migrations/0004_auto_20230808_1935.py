# Generated by Django 3.2.20 on 2023-08-08 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_address2',
        ),
    ]
