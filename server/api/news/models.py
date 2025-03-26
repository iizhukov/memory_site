from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


UserModel = get_user_model()

class NewsModel(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    content = RichTextField('Контент')
    published_at = models.DateTimeField('Время публикации', default=timezone.now)
    source = models.CharField('Источник', max_length=100, blank=True, null=True)
    author = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Автор'
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

    def __str__(self) -> str:
        return str(self.title)

