# Generated by Django 4.2.3 on 2023-08-22 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_rename_profil_photo_user_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='photo',
            new_name='image',
        ),
    ]
