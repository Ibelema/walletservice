from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Wallet(models.Model):
    CURRENCY_CHOICES = [
        ('ngn', 'NGN'),
        ('eur', 'EUR'),
        ('usd', 'USD')
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    wallet_id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=4, choices=CURRENCY_CHOICES, default='NGN')
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=CustomUser)
def create_wallet(sender, created, instance, **kwargs):
    if created:
        Wallet.objects.create(user=instance)

class WalletTransaction(models.Model):
    TRANSACTION_CHOICES = (
        ('deposit', 'DEPOSIT'),
        ('transfer', 'TRANSFER'),
    )
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
   
    transaction_type = models.CharField(
        max_length=100,
        choices = TRANSACTION_CHOICES,
        default=''               
    )
    
    amount = models.DecimalField(max_digits=13, decimal_places=2, default=0.0)

    timestamp = models.DateTimeField(auto_now_add=True)

    description = models.CharField(max_length=200, default='')

    source = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transfer')

    destination = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='deposit')

