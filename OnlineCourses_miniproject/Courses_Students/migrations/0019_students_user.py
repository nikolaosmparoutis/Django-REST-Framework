# Generated by Django 3.0.7 on 2020-06-12 04:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Courses_Students', '0018_auto_20200611_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
