from django.contrib import admin
from .models import CustomUser, Wallet, WalletTransaction
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Wallet)
admin.site.register(WalletTransaction)