# Generated by Django 3.2.5 on 2022-04-05 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='adboard',
            table='ad_board',
        ),
        migrations.AlterModelTable(
            name='addocument',
            table='adfile_board',
        ),
    ]