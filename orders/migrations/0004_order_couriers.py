# Generated by Django 3.2.3 on 2021-06-14 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0003_couriers'),
        ('orders', '0003_remove_order_stripe_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='couriers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='couriers.couriers', verbose_name='Курьер'),
        ),
    ]
