# Generated by Django 4.0.2 on 2022-08-11 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_button_about_button_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='button_content',
        ),
        migrations.RemoveField(
            model_name='about',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='coppyright',
            name='title',
        ),
        migrations.AddField(
            model_name='coppyright',
            name='text_color',
            field=models.CharField(blank=True, max_length=255, verbose_name='Text Color'),
        ),
        migrations.AddField(
            model_name='coppyright',
            name='theme_color',
            field=models.CharField(blank=True, max_length=255, verbose_name='Theme Color'),
        ),
        migrations.AddField(
            model_name='coppyright',
            name='title_color',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title Color'),
        ),
    ]
