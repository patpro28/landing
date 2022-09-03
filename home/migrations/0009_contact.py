# Generated by Django 4.0.7 on 2022-08-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_class_name_remove_class_student_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, verbose_name='Name')),
                ('img', models.CharField(blank=True, max_length=1024, verbose_name='Image')),
                ('link', models.CharField(blank=True, max_length=1024, verbose_name='Link')),
            ],
        ),
    ]