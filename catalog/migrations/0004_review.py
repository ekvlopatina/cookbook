# Generated by Django 3.0.5 on 2020-06-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200609_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ваше имя')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-date'],
            },
        ),
    ]