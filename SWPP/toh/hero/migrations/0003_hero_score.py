# Generated by Django 2.1.2 on 2018-10-17 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
