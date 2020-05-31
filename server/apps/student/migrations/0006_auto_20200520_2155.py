# Generated by Django 3.0.5 on 2020-05-20 21:55

import apps.student.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0005_student_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=apps.student.models.PathAndRename('students/profile_pictures'), verbose_name='Photo de profil'),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]