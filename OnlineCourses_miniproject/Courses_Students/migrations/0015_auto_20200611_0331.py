# Generated by Django 3.0.7 on 2020-06-11 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses_Students', '0014_auto_20200611_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='belongs_to_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='Courses_Students.CourseCategory'),
        ),
    ]
