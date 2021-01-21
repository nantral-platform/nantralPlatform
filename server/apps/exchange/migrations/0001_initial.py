# Generated by Django 3.0.8 on 2021-01-21 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0003_auto_20210121_1041'),
        ('student', '0002_rename_dd_cursus_add_alternant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('got', models.ForeignKey(limit_choices_to={'course_type': 'OD'}, on_delete=django.db.models.deletion.CASCADE, related_name='got_by', to='academic.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
                ('wanted', models.ManyToManyField(limit_choices_to={'course_type': 'OD'}, related_name='wanted_by', to='academic.Course')),
            ],
        ),
    ]