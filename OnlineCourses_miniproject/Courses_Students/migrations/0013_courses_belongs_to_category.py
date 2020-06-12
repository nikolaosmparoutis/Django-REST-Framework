# Generated by Django 3.0.7 on 2020-06-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses_Students', '0012_coursecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='belongs_to_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Courses_Students.CourseCategory'),
        ),
    ]
