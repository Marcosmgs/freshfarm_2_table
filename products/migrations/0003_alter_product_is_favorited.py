# Generated by Django 3.2.20 on 2023-08-06 16:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20230804_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_favorited',
            field=models.ManyToManyField(blank=True, default=False, related_name='my_favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]