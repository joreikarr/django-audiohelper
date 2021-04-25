from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.files import File

from audiohelper import settings


class text_to_speech_Data(models.Model):
    audio_name = models.TextField('Название дорожки')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.audio_name

    def save_file(self):
        self.audio_file.save(self.audio_name, self.audio_file)

    class Meta:
        verbose_name = 'Аудиофайл'
        verbose_name_plural = 'Аудиофайлы'
