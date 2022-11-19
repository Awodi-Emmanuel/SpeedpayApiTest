from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.fields import *
from rest_framework.serializers import Serializer, ValidationError


class DepositSerializer(Serializer):
    amount = DecimalField(max_digits=5, decimal_places=2,)
    description = CharField()
    class Meta:
        ref_name = None

class WithdrawSerializer(Serializer):
    amount = DecimalField(max_digits=5, decimal_places=2,)
    class Meta:
        ref_name = None