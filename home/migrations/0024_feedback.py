# Generated by Django 4.0.2 on 2022-08-16 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('infor', models.CharField(blank=True, max_length=1024, verbose_name='Information')),
                ('feedback', models.CharField(blank=True, max_length=1024, verbose_name='Feedback')),
                ('time', models.CharField(blank=True, max_length=1024, verbose_name='Time')),
            ],
        ),
    ]
