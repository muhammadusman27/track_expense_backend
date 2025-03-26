from django.urls import path
from user_management.views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]