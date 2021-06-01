# Generated by Django 3.2.3 on 2021-06-01 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendersAddress', models.CharField(max_length=300, verbose_name='Адрес отправителя')),
                ('sendersPhone', models.CharField(max_length=15, verbose_name='Телефон отправителя')),
                ('sendersFio', models.CharField(max_length=100, verbose_name='ФИО отправителя')),
                ('sendersDate', models.DateTimeField(blank=True, null=True, verbose_name='Дата забора заказа')),
                ('recipientAddress', models.CharField(max_length=300, verbose_name='Адрес получателя')),
                ('recipientPhone', models.CharField(max_length=15, verbose_name='Телефон получателя')),
                ('recipientFio', models.CharField(max_length=100, verbose_name='ФИО получателя')),
                ('recipientDate', models.DateTimeField(blank=True, null=True, verbose_name='Дата получения')),
                ('dateCreate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания заказа')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('status', models.CharField(choices=[('NEW', 'NEW'), ('ADOPTED', 'ADOPTED'), ('PICKEDUP', 'PICKEDUP'), ('DELIVERED', 'DELIVERED'), ('COMPLETED', 'COMPLETED')], default='NEW', max_length=20, verbose_name='Статус')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('value', models.PositiveIntegerField(default=0, verbose_name='Ценность')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.delivery', verbose_name='Вид доставки')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.payment', verbose_name='Способ оплаты')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('weight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.weight', verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
                'managed': True,
            },
        ),
    ]
