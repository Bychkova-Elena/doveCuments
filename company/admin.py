from django.contrib import admin
from .models import Contacts, Shedule, Payment, Delivery, Weight


admin.site.register(Contacts)
admin.site.register(Shedule)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Weight)
