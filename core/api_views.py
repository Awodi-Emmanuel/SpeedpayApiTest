from os import access
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Wallet, WalletTransaction, Account 

from .model_serializer import UserSerializer, WalletSerializer
from .input_serializer import DepositSerializer, WithdrawSerializer

from rest_framework.permissions import IsAuthenticated


class Login(APIView):
    permission_class = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key, "username": username})
        else:
            return Response({"error": "Wrong Credential"}, status=status.HTTP_400_BAD_REQUEST)

class Register(APIView):
    authentication_class = ()
    permission_class = ()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            rand_int = "0123456789"
            Account(
                user=user,
                current_bal=round(0.00, 2),
                previous_bal=round(0.00, 2),
                amount=rand_int
            ).save()
            account = Account.objects.get(user=user)
            return Response({
                'user': serializer.data,
                'account_number': account.amount,
                'balance': account.current_bal
            })

        else:
            return Response({'error': "Invalid Credential"})

class GetBalance(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if Account.objects.filter(user=request.user).exists():
            #TODO create account serializer to return account data
            return  Response({"response": "Account data!"})

        return  Response({"response": "You have not made any transactions with your account!"})
        

class Deposit(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **Kwargs):
        rcv_ser = DepositSerializer(data=self.request.data)
        if rcv_ser.is_valid():
            account =  Account.objects.get(user=request.user)

            account.previous_bal = account.current_bal  
            account.current_bal = rcv_ser.data['amount']
            account.save()
                  
            return Response({"message": "Credit successful"})

        else:
            return Response({"request": "Invalid payload!"})


class Withdraw(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **Kwargs):
        rcv_ser = WithdrawSerializer(data=self.request.data)
        if rcv_ser.is_valid():
            account =  Account.objects.get(user=request.user)

            account.previous_bal = account.current_bal
            #TODO: Add if satement to check amount is not greater than current balance  \
            print(account.current_bal)
            account.current_bal = float(account.current_bal) - float(rcv_ser.data['amount'])
            account.save()
                  
            return Response({"message": "Debit successful"})

        else:
            return Response({"request": "Invalid payload!"})
                    

