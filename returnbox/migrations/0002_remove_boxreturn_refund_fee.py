# Generated by Django 3.2.20 on 2023-10-09 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('returnbox', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxreturn',
            name='refund_fee',
        ),
    ]