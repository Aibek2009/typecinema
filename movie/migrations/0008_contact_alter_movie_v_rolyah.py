# Generated by Django 4.1.6 on 2023-02-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=12, verbose_name='телефон №1')),
                ('phone2', models.CharField(max_length=12, verbose_name='телефон №2')),
                ('address', models.CharField(help_text='например: Ленина, 316, \u200b90 филиалов с. Новопокровка, Ысык-Атинский район Чуйская область 1 этаж', max_length=222, verbose_name='адрес')),
                ('address_map', models.TextField(verbose_name='ссылка на местоположение')),
            ],
            options={
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.AlterField(
            model_name='movie',
            name='v_rolyah',
            field=models.ManyToManyField(blank=True, related_name='film_actor', to='movie.actors'),
        ),
    ]