# Generated by Django 4.0.6 on 2022-08-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_about_content_alter_achievement_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('infor', models.CharField(blank=True, max_length=1024, verbose_name='Information')),
                ('img', models.CharField(blank=True, max_length=1024, verbose_name='Image')),
                ('feedback', models.CharField(blank=True, max_length=1024, verbose_name='Feedback')),
                ('time', models.CharField(blank=True, max_length=1024, verbose_name='Time')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_link', models.CharField(max_length=1024, verbose_name='Background Link')),
            ],
        ),
        migrations.CreateModel(
            name='Narbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=1024, verbose_name='Name')),
                ('id_section', models.CharField(max_length=1024, verbose_name='ID')),
                ('link', models.CharField(max_length=1024, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Title')),
                ('content', models.CharField(max_length=1024, verbose_name='Content')),
                ('bg', models.CharField(blank=True, max_length=1024, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_color', models.CharField(max_length=1024, verbose_name='Theme Color')),
                ('text_color', models.CharField(max_length=1024, verbose_name='Text Color')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=1024, verbose_name='Image')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('content', models.CharField(blank=True, max_length=1024, verbose_name='Content')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=1024, verbose_name='Image')),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('content', models.CharField(blank=True, max_length=1024, verbose_name='Content')),
            ],
        ),
        migrations.DeleteModel(
            name='Achievement',
        ),
        migrations.DeleteModel(
            name='Classroom',
        ),
        migrations.DeleteModel(
            name='CoppyRight',
        ),
        migrations.DeleteModel(
            name='HomeButton',
        ),
        migrations.DeleteModel(
            name='HomeContent',
        ),
        migrations.DeleteModel(
            name='Navigation',
        ),
        migrations.DeleteModel(
            name='New',
        ),
        migrations.RemoveField(
            model_name='about',
            name='img_link',
        ),
        migrations.RemoveField(
            model_name='class',
            name='link',
        ),
        migrations.RemoveField(
            model_name='class',
            name='note',
        ),
        migrations.RemoveField(
            model_name='class',
            name='title',
        ),
        migrations.AddField(
            model_name='about',
            name='img_1',
            field=models.CharField(default='#', max_length=1024, verbose_name='Image 1'),
        ),
        migrations.AddField(
            model_name='about',
            name='img_2',
            field=models.CharField(default='#', max_length=1024, verbose_name='Image 2'),
        ),
        migrations.AddField(
            model_name='class',
            name='student',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='time',
            field=models.CharField(blank=True, max_length=1024, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='about',
            name='content',
            field=models.CharField(max_length=1024, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=1024, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=1024, verbose_name='Name'),
        ),
    ]