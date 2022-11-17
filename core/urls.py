from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .api_views import AuthViewset
    # TransferViewset
    


router = DefaultRouter()
router.register('auth', AuthViewset, basename='auth')
router.register('register/', RegisterVieset, basename=''),
router.register('login/', LoginViewset, basename=''),
router.register('wallet_info/', WalletInfo, basename=''),
router.register('deposit/', DepositFunds, basename=''),
router.register('deposit/verify/<str:reference>/', VerifyDeposit, basename=''),




urlpatterns = [
    
]

urlpatterns += router.urls