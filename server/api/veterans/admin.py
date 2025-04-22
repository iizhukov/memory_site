from django.contrib import admin

from django import forms
from django.utils.html import format_html
from django_ckeditor_5.widgets import CKEditor5Widget
from api.veterans import models


class NoteAdminForm(forms.ModelForm):
    text = forms.CharField(label="Текст записки", widget=CKEditor5Widget())

    class Meta:
        model = models.NoteModel
        fields = '__all__'


@admin.register(models.NoteModel)
class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm

    list_display = ('veteran_link', 'created_at', 'edit')
    list_filter = ('created_at',)
    search_fields = ('veteran__name', 'text')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    filter_horizontal = ()
    raw_id_fields = ('veteran',)
    fieldsets = (
        (None, {
            'fields': ('veteran', 'text')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def veteran_link(self, obj):
        if hasattr(obj, "veteran"):
            url = f"/admin/veterans/veteranmodel/{obj.veteran.id}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.veteran)
        
        return format_html('Ветеран не указан')

    veteran_link.short_description = 'Ветеран' # type: ignore
    veteran_link.admin_order_field = 'veteran__name' # type: ignore

    def edit(self, obj):
        url = f"/admin/veterans/notemodel/{obj.pk}/change/"
        return format_html('<a href="{}">{}</a>', url, "Редактировать")

    edit.short_description = "Редактировать" # type: ignore


class VeteranAdminForm(forms.ModelForm):
    pass

    class Meta:
        model = models.VeteranModel
        fields = '__all__'


@admin.register(models.VeteranModel)
class VeteranAdmin(admin.ModelAdmin):
    form = VeteranAdminForm

    list_display = ('name', 'surname', 'patronymic', 'birthday', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'surname', 'patronymic', 'birthday')
    readonly_fields = ('created_at', 'display_image')
    date_hierarchy = 'created_at'
    filter_horizontal = ()
    fieldsets = (
        (None, {
            'fields': ('name', 'surname', 'patronymic', 'birthday', 'image', 'display_image')
        }),
        ('Даты', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="200" />', obj.image.url)
        return "-"
 
    display_image.short_description = 'Фото' # type: ignore
