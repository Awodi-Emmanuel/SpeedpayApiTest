# from django.contrib import admin
# from .models import Wallet, WalletTransaction
# Register your models here.

# from models.implementation import (
#     Wallet,
#     WalletTransaction
# )

# admin.site.register(Wallet)
# class WalletAdmin(admin.ModelAdmin):
#     pass


# admin.site.register(WalletTransaction)
# class WalletTransaction(admin.ModelAdmin):
#     pass

from django.contrib import admin
from .models import Wallet, WalletTransaction
# Register your models here.

admin.site.register(Wallet)
admin.site.register(WalletTransaction)