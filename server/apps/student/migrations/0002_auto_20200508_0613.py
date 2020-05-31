# Generated by Django 3.0.5 on 2020-05-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='double_degree',
            field=models.CharField(blank=True, choices=[('I-A', 'Ingénieur-Architect'), ('A-I', 'Architect-Ingenieur'), ('I-M', 'Ingenieur-Manager'), ('M-I', 'Manager-Ingénieur'), ('I-O', 'Ingénieur-Officier'), ('O-I', 'Officier-Ingénieur')], max_length=200, null=True, verbose_name='Double-cursus'),
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('Gen', 'Eleve ingenieur generaliste'), ('Iti', 'Eleve ingenieur de specialité'), ('Mas', 'Eleve en master'), ('Doc', 'Doctorant')], default='Gen', max_length=200, verbose_name='Filliere'),
            preserve_default=False,
        ),
    ]