# Generated by Django 3.2.9 on 2021-11-29 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='progile_photo',
            new_name='profile_photo',
        ),
    ]