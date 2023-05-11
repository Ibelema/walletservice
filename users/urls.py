from django.urls import path
from .views import signup, userinfo, wallet_info
urlpatterns = [
    path('signup/', signup, name='signup'),
#    path('login/', login, name='login'),
 #   path('api-token-auth/', obtain_auth_token, name='api_token_auth')
    path('user-info/', userinfo, name='userinfo'),
    path('walletinfo/<str:wallet_id>/', wallet_info, name='wallet_info')
]