# Generated by Django 4.2.3 on 2023-08-03 23:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_review_second_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='second_review',
        ),
        migrations.AddField(
            model_name='review',
            name='self_review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='review.review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192, null=True, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='review',
            name='headline',
            field=models.CharField(max_length=128, null=True, verbose_name='Intitulé'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.ticket'),
        ),
        migrations.AlterField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='time_edited',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
