# Generated by Django 3.2.9 on 2021-12-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('litreview', '0007_ticket_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='answered',
            field=models.CharField(default='False', max_length=10),
        ),
    ]