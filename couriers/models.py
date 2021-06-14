from django.db import models
from users.models import User

class Applications(models.Model):
    # Заявки #

    fio = models.CharField("ФИО", max_length=100)
    phone = models.CharField("Телефон", max_length=15)

    def __str__(self):
        return '%s, %s' % (self.fio,  self.phone)

    class Meta:
        db_table = 'applications'
        managed = True
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class Couriers(models.Model):
    # Курьеры #

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.user)

    class Meta:
        db_table = 'couriers'
        managed = True
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'
