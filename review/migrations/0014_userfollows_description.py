# Generated by Django 4.2.3 on 2023-08-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0013_alter_userfollows_followed_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfollows',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
