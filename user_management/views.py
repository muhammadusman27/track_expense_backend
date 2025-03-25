from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from user_management.serializers import UserSerializer
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@api_view(['POST'])
def login(request):
    print('data = ', request.data)
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    print(user)
    if user is not None:
        token = RefreshToken.for_user(user)
        print(token)
        return Response(data={"data": token, "message": "invalid credentials."}, status=HTTP_200_OK)
    else:
        return Response(data={"data": {}, "message": "invalid credentials."}, status=HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def signup(request):
    data = request.data
    user = UserSerializer(data=data)
    if user.is_valid():
        user.save()
        return Response(data=user.data, status=HTTP_200_OK)
    else:
        return Response(data=user.errors, status=HTTP_400_BAD_REQUEST)