# Generated by Django 5.0.1 on 2024-02-08 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_rename_catigory_amount_catigory_catigory'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='main_logo',
            field=models.ImageField(default=1, upload_to='image_logo_main/', verbose_name='Главное лого'),
            preserve_default=False,
        ),
    ]
