# Generated by Django 4.0.5 on 2022-06-25 12:55

from django.db import migrations, models
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', martor.models.MartorField(verbose_name='description')),
                ('priority', models.IntegerField(default=0, verbose_name='priority')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title')),
            ],
        ),
    ]