# Generated by Django 3.2.9 on 2021-12-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litreview', '0004_auto_20211206_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Télécharger fichier'),
        ),
    ]
