# Generated by Django 4.0.2 on 2022-08-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Title')),
                ('content', models.CharField(max_length=1024, verbose_name='Content')),
                ('bg', models.CharField(max_length=1024, verbose_name='Image')),
            ],
        ),
    ]