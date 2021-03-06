# Generated by Django 3.2.5 on 2022-04-11 14:38

from django.db import migrations, models
import member.validators


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_user_is_social_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True, validators=[member.validators.validate_no_special_characters], verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(blank=True, max_length=4, null=True, validators=[member.validators.validate_age], verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=2, null=True, validators=[member.validators.validate_gender], verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_social_login',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='소셜로그인여부'),
        ),
    ]
