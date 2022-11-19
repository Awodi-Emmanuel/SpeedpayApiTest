from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# creat model here

class Account(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount: models.CharField = models.CharField(max_length=10, null=True, blank=True)
    current_bal: models.DecimalField = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    previous_bal: models.DecimalField = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at:  models.DateField = models.DateField(default=timezone.now, null=True)


class Wallet(models.Model):
    user: models.OneToOneField = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    amount: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    acount_no: models.CharField = models.CharField(max_length=100, null=True)
    current_bal: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at:  models.DateField = models.DateField(default=timezone.now, null=True)

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.user.__str__()

    

class WalletTransaction(models.Model):
    wallet: models.ForeignKey = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    description: models.TextField = models.TextField(blank=True, null=True)
    amount: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    destination_no: models.CharField = models.CharField(max_length=100, null=True)
    status: models.CharField = models.CharField(max_length=100, null=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        # abstract = True

        def __str__(self):
            return self.wallet.user.__str__()

        
    