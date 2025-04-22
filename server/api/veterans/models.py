from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from api.storages import MediaStorage


class VeteranModel(models.Model):
    name = models.CharField(
        "Имя", max_length=100,
    )
    surname = models.CharField(
        "Фамилия", max_length=100,
    )
    patronymic = models.CharField(
        "Отчество", max_length=100,
        null=True, blank=True
    )

    birthday = models.DateField(
        "День рождения",
        null=True, blank=True
    )

    image = models.ImageField(
        "Загрузить фото", upload_to="veterans/",
        storage=MediaStorage(),
        null=True, blank=True
    )

    is_vov_veteran = models.BooleanField(
        "Ветеран Великой Отечественной войны",
        default=False
    )

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Ветеран"
        verbose_name_plural = "Ветераны"

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.patronymic}"


class NoteModel(models.Model):
    veteran = models.ForeignKey(
        VeteranModel, on_delete=models.SET_NULL,
        verbose_name="Ветеран",
        null=True, blank=False
    )

    text = CKEditor5Field("Текст")

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Записка"
        verbose_name_plural = "Записки"

    def __str__(self) -> str:
        return str(self.veteran)
