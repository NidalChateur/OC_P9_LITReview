# Generated by Django 4.2.3 on 2023-07-10 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]