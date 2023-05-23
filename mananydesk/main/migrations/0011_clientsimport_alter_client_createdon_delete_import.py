# Generated by Django 4.2.1 on 2023-05-22 23:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_alter_client_createdon_import'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 5, 23, 0, 48, 49, 595808))),
                ('imported', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='imports/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='createdon',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 23, 0, 48, 49, 594808)),
        ),
        migrations.DeleteModel(
            name='Import',
        ),
    ]