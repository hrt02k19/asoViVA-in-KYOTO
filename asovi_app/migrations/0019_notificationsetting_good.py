# Generated by Django 3.1.3 on 2021-01-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asovi_app', '0018_auto_20210102_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationsetting',
            name='good',
            field=models.BooleanField(default=True),
        ),
    ]
