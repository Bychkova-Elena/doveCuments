from django.contrib import admin
from .models import Order

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ExportActionMixin


class OrderResource(resources.ModelResource):
  
    class Meta:
        model = Order

@admin.register(Order)
class OrderAdmin(ImportExportActionModelAdmin):
    resource_class = OrderResource
    list_filter = ("status", "couriers",)
    actions = ["changeOnADOPTED",
               "changeOnPICKEDUP", "changeOnDELIVERED", "changeOnCOMPLETED"]

    def changeOnADOPTED(self, request, queryset):
        #Изменить статус на принят#
        row_update = queryset.update(status='ADOPTED')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnPICKEDUP(self, request, queryset):
        #Изменить статус на забран#
        row_update = queryset.update(status='PICKEDUP')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnDELIVERED(self, request, queryset):
        #Изменить статус на доставлен#
        row_update = queryset.update(status='DELIVERED')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    def changeOnCOMPLETED(self, request, queryset):
        #Изменить статус на подтверждено#
        row_update = queryset.update(status='COMPLETED')
        if row_update == 1:
            message_bit = "The status of 1 entry has been changed"
        else:
            message_bit = f"The status of {row_update} entries has been changed"
        self.message_user(request, f"{message_bit}")

    changeOnADOPTED.short_description = "Заявка принята"
    changeOnADOPTED.allowed_permissions = ('change', )

    changeOnPICKEDUP.short_description = "Заявка забрана"
    changeOnPICKEDUP.allowed_permissions = ('change', )

    changeOnDELIVERED.short_description = "Заявка доставлена"
    changeOnDELIVERED.allowed_permissions = ('change', )

    changeOnCOMPLETED.short_description = "Заявка подтверждена и закрыта"
    changeOnCOMPLETED.allowed_permissions = ('change', )
