from django.db import models

class Contacts(models.Model):
    # Контакты #

    phone = models.CharField("Телефон", max_length=15)
    email = models.EmailField(max_length = 254)
    address = models.CharField("Адрес", max_length=300)

    def __str__(self):
        return '%s, %s, %s' % (self.phone, self.email, self.address)

    class Meta:
        db_table = 'contacts'
        managed = True
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

class Payment(models.Model):
    # Способ оплаты #

    name = models.CharField("Наименование", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'payment'
        managed = True
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'


class Delivery(models.Model):
    # Вид доставки #

    name = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание")
    price = models.PositiveIntegerField(
        "Цена", default=0)

    def __str__(self):
        return '%s, %s' % (self.name, self.price)

    class Meta:
        db_table = 'delivery'
        managed = True
        verbose_name = 'Вид доставки'
        verbose_name_plural = 'Виды доставки'

class Weight(models.Model):
    # Вес #

    weight = models.CharField("Вес", max_length=100)
    price = models.PositiveIntegerField(
        "Цена", default=0)

    def __str__(self):
        return '%s, %s' % (self.weight, self.price)

    class Meta:
        db_table = 'weight'
        managed = True
        verbose_name = 'Вес'
        verbose_name_plural = 'Вес'