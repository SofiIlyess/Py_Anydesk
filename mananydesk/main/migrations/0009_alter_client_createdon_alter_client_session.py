# Generated by Django 4.2.1 on 2023-05-10 02:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_client_createdon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdon',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 3, 22, 35, 652440)),
        ),
        migrations.AlterField(
            model_name='client',
            name='session',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
