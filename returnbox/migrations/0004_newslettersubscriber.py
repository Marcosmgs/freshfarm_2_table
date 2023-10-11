# Generated by Django 3.2.20 on 2023-10-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnbox', '0003_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
