# Generated by Django 3.2.4 on 2021-06-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cameras',
            name='port',
            field=models.PositiveSmallIntegerField(default=80),
        ),
    ]