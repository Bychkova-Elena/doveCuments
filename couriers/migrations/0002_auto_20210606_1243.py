# Generated by Django 3.2.3 on 2021-06-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='Fio',
            new_name='fio',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='Phone',
            new_name='phone',
        ),
    ]
