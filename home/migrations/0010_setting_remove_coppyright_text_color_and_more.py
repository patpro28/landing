# Generated by Django 4.0.2 on 2022-08-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_about_button_content_remove_about_button_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_color', models.CharField(blank=True, max_length=255, verbose_name='Theme Color')),
                ('title_color', models.CharField(blank=True, max_length=255, verbose_name='Title Color')),
                ('text_color', models.CharField(blank=True, max_length=255, verbose_name='Text Color')),
            ],
        ),
        migrations.RemoveField(
            model_name='coppyright',
            name='text_color',
        ),
        migrations.RemoveField(
            model_name='coppyright',
            name='theme_color',
        ),
        migrations.RemoveField(
            model_name='coppyright',
            name='title_color',
        ),
        migrations.AddField(
            model_name='coppyright',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='tile'),
        ),
    ]