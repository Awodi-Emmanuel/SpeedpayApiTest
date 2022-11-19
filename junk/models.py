from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# creat model here
class Wallet(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    currency: models.CharField = models.CharField(max_length=50, null=True)
    created_at: models.CharField = models.DateField(default=timezone.now, null=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.user.__str__()

    

class WalletTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'deposit'),
        ('transfer', 'transfer'),
        ('withdraw', 'withdraw'),
    )

    wallet: models.ForeignKey = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    transaction_type: models.CharField(
        max_length=200, null=True,  choices=TRANSACTION_TYPES)
    amount: models.DecimalField(max_digits=100, default="pending")
    paysack_payment_reference: models.CharField = models.CharField(max_length=100, default='', blank=True)

    class Meta:
        # abstract = True

        def __str__(self):
            return self.wallet.user.__str__()

        
    