from django.urls import path
from .views import signup, userinfo, wallet_info, login, protected_endpoint, transaction_detail
urlpatterns = [
    path('signup/', signup, name='signup'),
#    path('login/', login, name='login'),
 #   path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    path('user-info/', userinfo, name='userinfo'),
    path('walletinfo/<str:wallet_id>/', wallet_info, name='wallet_info'),
    path('login/', login, name='login'),
    path('protect/', protected_endpoint, name='protected'),
    path('transaction/<str:transaction_id>/', transaction_detail, name=transaction_detail),
]