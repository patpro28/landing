# Generated by Django 4.0.6 on 2022-07-26 00:27

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_about_achievement_class_classroom_emath_homebutton_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=martor.models.MartorField(blank=True, verbose_name='content'),
        ),
    ]