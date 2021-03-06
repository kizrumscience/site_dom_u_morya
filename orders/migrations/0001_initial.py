# Generated by Django 3.2 on 2021-05-01 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0005_alter_house_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('phone', models.CharField(max_length=50, verbose_name='телефон')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house', verbose_name='дом')),
            ],
        ),
    ]
