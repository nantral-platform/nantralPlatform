# Generated by Django 3.0.5 on 2020-06-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name="Date de l'événement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name="Description de l'événement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='publicity',
            field=models.CharField(choices=[('Pub', 'Public - Visible par tous'), ('Mem', 'Membres - Visible uniquement par les membres du groupe')], max_length=200, verbose_name="Visibilité de l'événement"),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=200, verbose_name="Titre de l'événement"),
        ),
    ]
