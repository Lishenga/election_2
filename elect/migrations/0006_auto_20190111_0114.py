# Generated by Django 2.1.4 on 2019-01-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elect', '0005_auto_20190110_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
