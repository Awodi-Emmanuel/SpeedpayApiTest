
from drf_yasg import openapi  # type: ignore
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Wallet, WalletTransaction 



from .model_serializer import UserSerializer
from .input_serializer import DepositSerializer

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
            serializer.save()
            return Response(serializer.data)

        else:
            return Response({'error': "Invalid Credential"})

class WalletInfo(APIView):

    def get(self, request):
        wallet = Wallet.objects.get(user=request.user)
        print(wallet)
        data = WalletSerializer(wallet).data 
        return Response(data)  


    
class Deposit(APIView):

    def post(self, request, *args, **Kwargs):
        rcv_ser = DepositSerializer(data=self.request.data)
        if rcv_ser.is_valid():
            print(serializer)

            
            return True
        else:
            return Response({"request": "Invalid payload!"})
                    

