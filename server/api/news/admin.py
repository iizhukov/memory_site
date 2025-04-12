from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget

from api.news import models


@admin.register(models.GroupModel)
class GroupModel(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'display_image')
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'image', 'display_image', 'description')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="200" />', obj.image.url)
        return "-"
 
    display_image.short_description = 'Изображение' # type: ignore


@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_link', 'slug', 'created_at')
    list_filter = ('group', 'created_at')
    search_fields = ('name', 'group__name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'display_image')
    raw_id_fields = ('group',)
    fieldsets = (
        (None, {
            'fields': ('group', 'name', 'slug', 'image', 'display_image', 'description')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def group_link(self, obj):
        url = f"/admin/news/categorygroup/{obj.group.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.group.name)

    group_link.short_description = 'Группа' # type: ignore
    group_link.admin_order_field = 'group__name' # type: ignore

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    short_description.short_description = 'Описание' # type: ignore

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="200" />', obj.image.url)
        return "-"
 
    display_image.short_description = 'Изображение' # type: ignore


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label="Содержимое", widget=CKEditor5Widget())
    
    class Meta:
        model = models.NewsModel
        fields = '__all__'


@admin.register(models.NewsModel)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

    list_display = ('title', 'category_link', 'author')
    list_filter = ('category__group', 'category', 'published_at', 'source', 'created_at')

    search_fields = ('title', 'content', 'category__name')

    readonly_fields = ('created_at', 'updated_at', 'display_image')
    date_hierarchy = 'created_at'
    filter_horizontal = ()
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'display_image', 'content', 'category', 'is_published', 'source')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at', 'published_at'),
            'classes': ('collapse',)
        }),
    )

    def category_link(self, obj):
        url = f"/admin/news/category/{obj.category.id}/change/"
        return format_html('<a href="{}">{}</a>', url, obj.category.name)

    category_link.short_description = 'Категория' # type: ignore
    category_link.admin_order_field = 'category__name' # type: ignore

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="200" />', obj.image.url)
        return "-"
 
    display_image.short_description = 'Обложка' # type: ignore

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'category__group')

