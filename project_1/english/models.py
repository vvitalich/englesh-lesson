from django.db import models


class World(models.Model):

    id = models.AutoField(primary_key=True)
    value_russ = models.CharField(max_length=255, blank=True, null=True, verbose_name='Русский')
    value_eng = models.CharField(max_length=255, blank=True, null=True, verbose_name='English')
    transcription = models.CharField(max_length=255, blank=True, null=True, verbose_name='Транскрипция')
    reads_like = models.CharField(max_length=255, blank=True, null=True, verbose_name='Читается как')
    audio = models.FileField(upload_to='audio/', blank=True, null=True, verbose_name='Звук')
    picture = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Картинка')
    part_of_speech = models.CharField(max_length=255, blank=True, null=True, verbose_name='Часть речи')
    top = models.CharField(max_length=255, blank=True, null=True, verbose_name='Вхождение в ТОП')

    class Meta:
        verbose_name = "World"
        verbose_name_plural = "Worlds"

    def __str__(self):
        return self.value_russ

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

