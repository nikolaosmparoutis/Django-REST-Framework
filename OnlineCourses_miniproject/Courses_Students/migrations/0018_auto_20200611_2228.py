# Generated by Django 3.0.7 on 2020-06-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses_Students', '0017_auto_20200611_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsenrollstocourses',
            name='enrolls_to_courses',
            field=models.ManyToManyField(to='Courses_Students.Courses'),
        ),
    ]
