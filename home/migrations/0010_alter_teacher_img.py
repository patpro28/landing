# Generated by Django 4.0.2 on 2022-09-01 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(upload_to='teachers', verbose_name='Image'),
        ),
    ]
