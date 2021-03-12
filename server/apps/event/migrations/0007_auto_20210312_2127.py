# Generated by Django 3.0.8 on 2021-03-12 21:27

import apps.utils.upload
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20210312_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseevent',
            name='description',
            field=models.TextField(verbose_name="Description de l'événement"),
        ),
        migrations.AlterField(
            model_name='baseevent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.utils.upload.PathAndRename('posts/pictures'), verbose_name='Une image, une affiche en lien ?'),
        ),
        migrations.AlterField(
            model_name='baseevent',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 21, 27, 8, 737303), verbose_name='Date de publication'),
        ),
        migrations.AlterField(
            model_name='baseevent',
            name='title',
            field=models.CharField(max_length=200, verbose_name="Titre de l'événement"),
        ),
    ]