# Generated by Django 4.1.5 on 2023-01-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value_russ', models.CharField(blank=True, max_length=255, null=True, verbose_name='Русский')),
                ('value_eng', models.CharField(blank=True, max_length=255, null=True, verbose_name='English')),
                ('transcription', models.CharField(blank=True, max_length=255, null=True, verbose_name='Транскрипция')),
                ('reads_like', models.CharField(blank=True, max_length=255, null=True, verbose_name='Читается как')),
                ('audio', models.CharField(blank=True, max_length=255, null=True, verbose_name='Звук')),
                ('picture', models.CharField(blank=True, max_length=255, null=True, verbose_name='Картинка')),
                ('part_of_speech', models.CharField(blank=True, max_length=255, null=True, verbose_name='Часть речи')),
                ('top', models.CharField(blank=True, max_length=255, null=True, verbose_name='Вхождение в ТОП')),
            ],
            options={
                'verbose_name': 'World',
                'verbose_name_plural': 'Worlds',
            },
        ),
    ]
