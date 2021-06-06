from django.db import models

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
