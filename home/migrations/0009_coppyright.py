# Generated by Django 4.0.6 on 2022-08-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_new_button_link_alter_new_button'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoppyRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='tile')),
            ],
        ),
    ]
