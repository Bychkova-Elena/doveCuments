from django.contrib import admin
from .models import Contacts, Payment, Delivery, Weight


admin.site.register(Contacts)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Weight)
