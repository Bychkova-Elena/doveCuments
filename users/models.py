from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    fio = models.CharField("ФИО", max_length=100)
    phone = models.CharField("Телефон", max_length=15, null=True)
  
    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class AddressBook(models.Model):
    # адресная книга #

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE)
    address = models.CharField("Адрес", max_length=300)

    def __str__(self):
        return '%s, %s' % (self.user,  self.address)

    class Meta:
        app_label = 'auth'
        db_table = 'addressBook'
        managed = True
        verbose_name = 'Адресная книга'
        verbose_name_plural = 'Адресные книги'

class ProxyUser(User):
    pass

    class Meta:
         app_label = 'auth'
         proxy = True
         verbose_name = 'Пользователь'
         verbose_name_plural = 'Пользователи'