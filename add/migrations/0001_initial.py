# Generated by Django 3.2.5 on 2022-04-05 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('contents', models.TextField()),
                ('view_cnt', models.IntegerField(default=0)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('exp_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AdDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='AdFiles/')),
                ('originalName', models.CharField(max_length=200)),
                ('adBoard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add.adboard')),
            ],
        ),
    ]
