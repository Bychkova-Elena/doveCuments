from django.db import models
import django.utils.timezone
from users.models import User
from company.models import Payment, Delivery, Weight

class Order(models.Model):
    # Заказы #

    NEW = 'NEW'
    ADOPTED = 'ADOPTED'
    PICKEDUP = 'PICKEDUP'
    DELIVERED = 'DELIVERED'
    COMPLETED = 'COMPLETED'
    STATUS = [
        (NEW, 'NEW'),
        (ADOPTED, 'ADOPTED'),
        (PICKEDUP, 'PICKEDUP'),
        (DELIVERED, 'DELIVERED'),
        (COMPLETED, 'COMPLETED')
    ]

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.PROTECT, null=True, blank=True)
    sendersAddress = models.CharField("Адрес отправителя", max_length=300)
    sendersPhone = models.CharField("Телефон отправителя", max_length=15)
    sendersFio = models.CharField("ФИО отправителя", max_length=100)
    sendersDate = models.DateTimeField(
        "Дата забора заказа", blank=True, null=True)
    recipientAddress = models.CharField("Адрес получателя", max_length=300)
    recipientPhone = models.CharField("Телефон получателя", max_length=15)
    recipientFio = models.CharField("ФИО получателя", max_length=100)
    recipientDate = models.DateTimeField(
        "Дата получения", blank=True, null=True)
    payment = models.ForeignKey(
        Payment, verbose_name="Способ оплаты", on_delete=models.PROTECT)
    dateCreate = models.DateTimeField(
        "Дата создания заказа", default=django.utils.timezone.now)
    price = models.PositiveIntegerField(
        "Цена", default=0) 
    delivery = models.ForeignKey(
        Delivery, verbose_name="Вид доставки", on_delete=models.PROTECT)
    status = models.CharField("Статус",
                              max_length=20,
                              choices=STATUS,
                              default=NEW)
    comment = models.TextField("Комментарий", null=True, blank=True)
    weight = models.ForeignKey(
        Weight, verbose_name="Вес", on_delete=models.PROTECT)
    value = models.PositiveIntegerField(
        "Ценность", default=0)

    

    def __str__(self):
        return '%s, %s, %s,  %s' % (self.sendersAddress,  self.recipientAddress,  self.status, self.price)

    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'