from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


UserModel = get_user_model()


class CategoryGroupModel(models.Model):
    name = models.CharField(
        max_length=100, unique=True,
        validators=[MinLengthValidator(2)]
    )
    image = models.ImageField(upload_to='category_groups/')

    author = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Автор"
    )

    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.name)


class CategoryModel(models.Model):
    group = models.ForeignKey(
        CategoryGroupModel, on_delete=models.CASCADE,
        related_name='categories'
    )

    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )

    description = CKEditor5Field("Описание")
    
    author = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Автор"
    )

    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('group', 'name')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.group.name}-{self.name}")

        super().save(*args, **kwargs)

        def __str__(self):
            return f"{self.group.name} - {self.name}"


class NewsModel(models.Model):
    category = models.ForeignKey(
        CategoryModel,  on_delete=models.CASCADE,
        related_name='news'
    )

    title = models.CharField("Заголовок", max_length=255)
    content = CKEditor5Field("Контент")

    published_at = models.DateTimeField("Время публикации", default=timezone.now)

    source = models.CharField("Источник", max_length=100, blank=True, null=True)
    author = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Автор"
    )

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    objects = models.Manager()

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return str(self.title)

