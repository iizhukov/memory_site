from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from api.news.models import NewsModel


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = NewsModel
        fields = '__all__'


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm

    list_display = ('title', 'published_at', 'source', 'author')
    list_filter = ('published_at', 'source')

    search_fields = ('title', 'content')

    prepopulated_fields = {}

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'source', 'author')
        }),
        ('Даты', {
            'fields': ('published_at',),
            'classes': ('collapse',)
        }),
    )

