# Generated by Django 5.1.7 on 2025-03-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='education/', verbose_name='Фотография'),
        ),
    ]
