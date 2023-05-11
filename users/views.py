from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, WalletSerializer
from .models import Wallet
# Create your views here.

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        return Response({'RESPONSE':'Signup was successful', 'data':data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def userinfo(request):
    if request.method == 'GET':
        user = request.user
        serializer = UserSerializer(user)
        data = serializer.data
        return Response({'message':'this is the user information', 'data':data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def wallet_info(request, wallet_id):
    try:
        wallet = Wallet.objects.get(wallet_id=wallet_id)
    except Wallet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = WalletSerializer(wallet) 
            return Response(serializer.data)