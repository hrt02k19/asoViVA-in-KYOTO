# Generated by Django 3.1.3 on 2021-01-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asovi_app', '0022_auto_20210102_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationsetting',
            name='friend',
            field=models.BooleanField(default=True, verbose_name='通知設定:フレンドリクエスト'),
        ),
        migrations.AlterField(
            model_name='notificationsetting',
            name='reply',
            field=models.BooleanField(default=True, verbose_name='通知設定:返信'),
        ),
    ]
