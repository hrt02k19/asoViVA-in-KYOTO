# Generated by Django 3.1.3 on 2020-12-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asovi_app', '0004_auto_20201213_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='good',
            field=models.BooleanField(default=False),
        ),
    ]
