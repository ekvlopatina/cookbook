# Generated by Django 3.0.5 on 2020-06-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
