from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import Login, Register, WalletInfo, Deposit
    
    


router = DefaultRouter()




urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('account_info/', WalletInfo.as_view()),
    path('deposit/', Deposit.as_view())
]

urlpatterns += router.urls