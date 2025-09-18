"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django_ckeditor_5 import views as ckeditor5_views
from debug_toolbar.toolbar import debug_toolbar_urls


admin.site.site_header = 'Администрирование Сайта Ветеранов'
admin.site.site_title = 'Администрирование Сайта Ветеранов'
admin.site.index_title = 'Администрирование Сайта Ветеранов'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    path('ckeditor/upload/', ckeditor5_views.upload_file, name='ck_editor_5_upload_file'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()

