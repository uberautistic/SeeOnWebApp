# Generated by Django 5.1.2 on 2024-12-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_date_of_birth_user_is_calibrated'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Тип контента',
                'verbose_name_plural': 'Типы контента',
            },
        ),
        migrations.AlterModelOptions(
            name='watchlist',
            options={'verbose_name': 'Избранный фильм', 'verbose_name_plural': 'Вотчлист'},
        ),
    ]
