# Generated by Django 3.2.5 on 2022-04-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0002_auto_20220405_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='adboard',
            name='mainpotho',
            field=models.FileField(blank=True, null=True, upload_to='AdFiles/'),
        ),
        migrations.DeleteModel(
            name='AdDocument',
        ),
    ]
