from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer, WalletSerializer
from .models import Wallet, WalletTransaction
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
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

@api_view(['POST'])
def login(request):
    #authenticate user and generate JWT token.

    email = request.data.gett('email')
    password = request.data.get('password')

    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    data = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    user = request.user
    return Response({'message': f'Hello {user.email}!'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def transaction_detail(request, pk):
    try:
        transaction = WalletTransaction.objects.get(pk=pk)
    except WalletTransaction.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WalletTransactionSerializer(transaction, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={'error':'NOT FOUND'}, status=status.HTTP_400_BAD_REQUEST)