# Generated by Django 4.2.3 on 2023-08-09 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_alter_review_rating_alter_review_time_last_entry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='time_last_entry',
        ),
        migrations.AlterField(
            model_name='review',
            name='time_last_entry',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
