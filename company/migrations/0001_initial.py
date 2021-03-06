# Generated by Django 3.2.3 on 2021-06-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
                'db_table': 'contacts',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Вид доставки',
                'verbose_name_plural': 'Виды доставки',
                'db_table': 'delivery',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'verbose_name_plural': 'Способы оплаты',
                'db_table': 'payment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applications', models.CharField(max_length=100, verbose_name='Прием заявок')),
                ('callCentre', models.CharField(max_length=100, verbose_name='Контакт-центр')),
            ],
            options={
                'verbose_name': 'График работы',
                'verbose_name_plural': 'График работы',
                'db_table': 'shedule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=100, verbose_name='Вес')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Вес',
                'verbose_name_plural': 'Вес',
                'db_table': 'weight',
                'managed': True,
            },
        ),
    ]
