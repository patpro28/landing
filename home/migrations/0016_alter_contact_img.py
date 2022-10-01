# Generated by Django 4.0.7 on 2022-10-01 03:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_reason_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img',
            field=models.FileField(max_length=255, upload_to='social', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='Image'),
        ),
    ]
