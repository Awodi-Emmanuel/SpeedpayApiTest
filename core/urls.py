from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import Login, Register, GetBalance, Deposit, Withdraw
    
router = DefaultRouter()

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('balance/', GetBalance.as_view()),
    path('deposit/', Deposit.as_view()),
    path('withdraw/', Withdraw.as_view())
]

urlpatterns += router.urls