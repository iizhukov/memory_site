from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from api.storages import MediaStorage


class MemorialModel(models.Model):
    name = models.CharField(
        "Название", max_length=200
    )
    description = CKEditor5Field("Описание")

    address = models.CharField(
        "Адрес", max_length=200
    )
    
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    yandex_link = models.URLField("Ссылка на Яндекс.Карты")
    two_gis_link = models.URLField("Ссылка на 2ГИС")

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Памятник"
        verbose_name_plural = "Памятники"

    def __str__(self) -> str:
        return str(self.name)


class PhotoModel(models.Model):
    memorial = models.ForeignKey(
        MemorialModel, on_delete=models.CASCADE,
        related_name='photos'
    )

    image = models.ImageField(
        "Фото", upload_to='memorials/',
        storage=MediaStorage(),
    )

    objects = models.Manager()

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
    
    def __str__(self) -> str:
        return str(self.memorial)
