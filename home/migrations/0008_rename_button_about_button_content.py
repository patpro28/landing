# Generated by Django 4.0.6 on 2022-08-04 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_about_button_about_button'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='button',
            new_name='button_content',
        ),
    ]
