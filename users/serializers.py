from rest_framework import serializers
from .models import CustomUser, Wallet, WalletTransaction
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        Token.objects.create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['balance', 'currency', 'wallet_id']

class WalletTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = WalletTransaction
        fields = ['wallet', 'transaction_type', 'amount', 'timestamp', 'description', 'source', 'destination']