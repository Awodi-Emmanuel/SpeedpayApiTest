from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import Login, Register
    # TransferViewset
    


router = DefaultRouter()
# # router.register('auth', AuthViewset, basename='auth')
# router.register('register/', Register.as_view()),
# router.register('login/', Login.as_view()),
# router.register('wallet_info/', WalletInfo, basename=''),
# router.register('deposit/', DepositFunds, basename=''),
# router.register('deposit/verify/<str:reference>/', VerifyDeposit, basename=''),




urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
]

urlpatterns += router.urls