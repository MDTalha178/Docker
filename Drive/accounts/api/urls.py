from django.urls import path, include
from accounts.api.views import*
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', CustomAuthToken.as_view(), name = 'login'),
    path('register/',register, name = 'register'),
    path('logout/',logout, name = 'logout'),
]