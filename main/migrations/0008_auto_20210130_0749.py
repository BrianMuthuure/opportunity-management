# Generated by Django 3.1.5 on 2021-01-30 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_opportunity_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]