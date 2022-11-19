from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.fields import *
from rest_framework.serializers import Serializer, ValidationError


class DepositSerializer(Serializer):
    amount = IntegerField()
    description = CharField()
    destination_no = CharField()

    class Meta:
        ref_name = None