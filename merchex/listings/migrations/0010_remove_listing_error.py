# Generated by Django 4.2.3 on 2023-07-10 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_listing_error'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='error',
        ),
    ]