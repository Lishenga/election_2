# Generated by Django 2.1.2 on 2018-12-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote_token',
            name='election_id',
            field=models.IntegerField(default=0),
        ),
    ]