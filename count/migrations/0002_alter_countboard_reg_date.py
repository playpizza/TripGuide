# Generated by Django 3.2.5 on 2022-04-10 13:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countboard',
            name='reg_date',
            field=models.DateField(default=django.utils.timezone.now, unique=True),
        ),
    ]
