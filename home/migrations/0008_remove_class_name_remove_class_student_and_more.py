# Generated by Django 4.0.6 on 2022-08-22 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_feedback_homebanner_narbar_reason_setting_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='name',
        ),
        migrations.RemoveField(
            model_name='class',
            name='student',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='class',
            name='time',
        ),
        migrations.AddField(
            model_name='class',
            name='class_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='img_1',
            field=models.CharField(max_length=1024, verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='about',
            name='img_2',
            field=models.CharField(max_length=1024, verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_color',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Text Color'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='theme_color',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Theme Color'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='content',
            field=models.TextField(blank=True, max_length=1024, verbose_name='Content'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1024, verbose_name='Name')),
                ('student', models.CharField(blank=True, max_length=1024, verbose_name='Student')),
                ('teacher', models.CharField(blank=True, max_length=1024, verbose_name='Teacher')),
                ('time', models.CharField(blank=True, max_length=1024, verbose_name='Time')),
                ('room_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addition', to='home.class')),
            ],
        ),
    ]