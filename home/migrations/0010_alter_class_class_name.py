# Generated by Django 4.0.6 on 2022-08-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_class_class_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_name',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]