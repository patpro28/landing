# Generated by Django 4.0.7 on 2022-09-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_class_class_name_alter_student_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img',
            field=models.ImageField(upload_to='social', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='img',
            field=models.ImageField(upload_to='feedback', verbose_name='avatar'),
        ),
    ]