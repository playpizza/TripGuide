# Generated by Django 3.2.5 on 2022-04-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_rename_mainpotho_eventboard_mainphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventboard',
            name='image_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]