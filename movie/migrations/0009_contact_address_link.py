# Generated by Django 4.1.6 on 2023-02-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_contact_alter_movie_v_rolyah'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address_link',
            field=models.CharField(max_length=100, null=True, verbose_name='link address'),
        ),
    ]
