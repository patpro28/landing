# Generated by Django 4.0.6 on 2022-08-03 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_homecontent_title4_remove_homecontent_title5_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeImg',
        ),
        migrations.AddField(
            model_name='homecontent',
            name='path_1',
            field=models.CharField(blank=True, max_length=1024, verbose_name='path 1'),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='path_2',
            field=models.CharField(blank=True, max_length=1024, verbose_name='path 2'),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='path_3',
            field=models.CharField(blank=True, max_length=1024, verbose_name='path 3'),
        ),
    ]
