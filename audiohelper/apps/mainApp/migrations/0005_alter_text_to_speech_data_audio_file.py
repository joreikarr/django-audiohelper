# Generated by Django 3.2 on 2021-04-19 17:14

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_alter_text_to_speech_data_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text_to_speech_data',
            name='audio_file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Роман\\PycharmProjects\\audiohelper\\audiohelper\\media'), upload_to=''),
        ),
    ]
