# Generated by Django 3.1.5 on 2021-01-30 04:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210129_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
