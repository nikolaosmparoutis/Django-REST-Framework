# Generated by Django 3.0.7 on 2020-06-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses_Students', '0004_auto_20200609_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsenrollstocourses',
            name='enrolls_to_courses',
            field=models.ManyToManyField(blank=True, to='Courses_Students.Courses'),
        ),
    ]
