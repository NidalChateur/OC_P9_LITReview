# Generated by Django 4.2.3 on 2023-08-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_ticket_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='time_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time_edited',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]