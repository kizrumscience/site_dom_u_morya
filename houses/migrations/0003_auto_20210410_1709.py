# Generated by Django 3.2 on 2021-04-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_house_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='date',
            field=models.DateField(default='2020-01-01', verbose_name='дата'),
        ),
    ]
