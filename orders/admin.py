from django.contrib import admin
from .models import Order, Status, Payment, Delivery, Weight


admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Payment)
admin.site.register(Delivery)
admin.site.register(Weight)
