from rest_framework import serializers
from django.db.models import Sum
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Wallet, WalletTransaction 
from rest_framework.serializers import CharField, IntegerField, ListSerializer
from django.conf import settings
import requests
from rest_framework.serializers import ModelSerializer 




class UserSerializer(ModelSerializer):
    """
    Serializer to validate and create a new user
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class WalletSerializer(ModelSerializer):
    id = IntegerField()

    class Meta:
        model = Wallet
        fields =(
            "user",
            "amount",
            "acount_no",
            "current_bal",
            "created_at",
        )

class WalletTransactionSerializer(ModelSerializer):
    id = IntegerField()

    class Meta:
        model = WalletTransaction
        fields =(
            "wallet",
            "description",
            "amount",
            "destination_no",
            "status",
            "created_at",
        )

    



    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         return value 
    #     raise serializers.ValidationError({"detail": "Email not found"})

    # def save(self):
    #     user = self.context['requests'].user
    #     wallet = Wallet.objects.get(user=user)
    #     data = self.validated_data
    #     print(data)
    #     url = "https://api.paystack.co/transaction/initialize"
    #     headers = {"authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
    #     r = requests.post(url, headers=headers, data=data)
    #     response = r.json()
    #     print(response)

    #     WalletTransaction.objects(
    #         wallet=wallet,
    #         description=description,
    #         transaction_type = "deposit",
    #         amount = data['amout'],
    #         # paystack_payment_refernce=response['data']['reference'],
    #         status="pending"
    #     )
    #     return response
