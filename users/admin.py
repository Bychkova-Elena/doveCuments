from django.contrib import admin
from .models import  AddressBook, ProxyUser

admin.site.register(ProxyUser)
admin.site.register(AddressBook)