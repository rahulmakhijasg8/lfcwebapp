# Generated by Django 3.2.9 on 2021-11-18 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_fixtures_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixtures',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
