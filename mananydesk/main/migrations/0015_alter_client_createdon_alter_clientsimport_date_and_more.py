# Generated by Django 4.2.1 on 2023-05-23 00:34

import datetime
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_client_createdon_alter_clientsimport_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='createdon',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 1, 34, 19, 481343)),
        ),
        migrations.AlterField(
            model_name='clientsimport',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 1, 34, 19, 481343)),
        ),
        migrations.AlterField(
            model_name='clientsimport',
            name='file',
            field=models.FileField(upload_to='Clients/', validators=[main.validators.validate_file]),
        ),
    ]
