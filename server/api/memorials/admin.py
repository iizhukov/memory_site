from django.contrib import admin

from django import forms
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget
from api.memorials import models


class MemorialAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = models.MemorialModel
        fields = '__all__'


class PhotoInline(admin.TabularInline):
    model = models.PhotoModel
    extra = 1
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html('<img src="{}" height="150" />', obj.image.url) if obj.image else None
    image_preview.short_description = 'Изображение'


@admin.register(models.MemorialModel)
class MemorialAdmin(admin.ModelAdmin):
    form = MemorialAdminForm

    list_display = ('name', 'address', 'latitude', 'longitude', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'address', 'description')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    filter_horizontal = ()
    inlines = [PhotoInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'address', 'latitude', 'longitude', 'yandex_link', 'two_gis_link')
        }),
        ('Дополнительно', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

