# Generated by Django 3.1.3 on 2021-01-01 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asovi_app', '0017_auto_20210102_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationsetting',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='notificationsetting',
            name='good',
        ),
        migrations.RemoveField(
            model_name='notificationsetting',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='notificationsetting',
            name='save',
        ),
    ]
