# Generated by Django 2.1.4 on 2019-01-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elect', '0008_winner_position_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='position_name',
            field=models.CharField(default='JESUS', max_length=255),
        ),
    ]
