# Generated by Django 4.0.6 on 2022-07-26 00:30

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_about_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='content',
            field=martor.models.MartorField(blank=True, verbose_name='content'),
        ),
    ]
