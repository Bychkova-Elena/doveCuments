from django.db import models
import django.utils.timezone
from users.models import User, AddressBook
from company.models import Payment, Delivery, Weight


class Status(models.Model):
    # Статусы #

    name = models.CharField("Наименование", max_length=150)   

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'status'
        managed = True
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    # Заказы #

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.PROTECT, null=True)
    sendersAddress = models.CharField("Адрес отправителя", max_length=300)
    sendersPhone = models.CharField("Телефон отправителя", max_length=15)
    sendersFio = models.CharField("ФИО отправителя", max_length=100)
    recipientAddress = models.CharField("Адрес получателя", max_length=300)
    recipientPhone = models.CharField("Телефон получателя", max_length=15)
    recipientFio = models.CharField("ФИО получателя", max_length=100)
    payment = models.OneToOneField(
        Payment, verbose_name="Способ оплаты", on_delete=models.PROTECT)
    dateCreate = models.DateTimeField(
        "Дата создания заказа", default=django.utils.timezone.now)
    dateReceive = models.DateTimeField(
        "Дата получения")
    price = models.PositiveIntegerField(
        "Цена", default=0) 
    delivery = models.OneToOneField(
        Delivery, verbose_name="Вид доставки", on_delete=models.PROTECT)
    status = models.OneToOneField(
        Status, verbose_name="Статус", on_delete=models.PROTECT)
    comment = models.TextField("Комментарий", null=True, blank=True)
    weight = models.OneToOneField(
        Weight, verbose_name="Вес", on_delete=models.PROTECT)
    value = models.PositiveIntegerField(
        "Ценность", default=0)

    

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.sendersAddress,  self.recipientAddress,  self.dateReceive, self.status, self.price)

    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'