# Generated by Django 5.0.1 on 2024-02-05 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_about_alter_settings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catigory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catigory_amount', models.CharField(max_length=255, verbose_name='Название Категория')),
            ],
            options={
                'verbose_name': '3) Категория',
                'verbose_name_plural': '4) Категории',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': '2) Об о мне', 'verbose_name_plural': '2) Об о мне'},
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.catigory', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
