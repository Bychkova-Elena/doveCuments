import graphene
from graphene_django import DjangoObjectType

from .models import Contacts


class ContactsType(DjangoObjectType):
    # Список контактов #

    class Meta:
        model = Contacts


class Query(graphene.ObjectType):

    all_contacts = graphene.List(ContactsType)

    def resolve_all_contacts(self, info, **kwargs):
        return Contacts.objects.all()
