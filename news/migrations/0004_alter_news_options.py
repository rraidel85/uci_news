# Generated by Django 5.0.3 on 2024-03-19 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias'},
        ),
    ]
