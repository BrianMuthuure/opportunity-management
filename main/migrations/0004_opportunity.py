# Generated by Django 3.1.5 on 2021-01-29 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_account_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.PositiveSmallIntegerField(default=1)),
                ('stage', models.CharField(choices=[('Discovery', 'Discovery'), ('Proposal Shared', 'Proposal Shared'), ('Negotiations', 'Negotiations')], max_length=150)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
            ],
        ),
    ]
