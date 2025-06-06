# Generated by Django 5.1.7 on 2025-04-12 08:27

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VeteranModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='veterans/', verbose_name='Фото')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Ветеран',
                'verbose_name_plural': 'Ветераны',
            },
        ),
        migrations.CreateModel(
            name='NoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('veteran', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veterans.veteranmodel', verbose_name='Ветеран')),
            ],
            options={
                'verbose_name': 'Записка',
                'verbose_name_plural': 'Записки',
            },
        ),
    ]
