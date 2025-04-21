from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from user_management.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# Create your views here.

@api_view(['POST'])
def login(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])

    if user is not None:
        token = RefreshToken.for_user(user)
        data = {
        'refresh': str(token),
        'access': str(token.access_token),
    }
        return Response(data={"data": data, "message": ""}, status=HTTP_200_OK)
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
    

def refresh_access_token(refresh_token_str):
    try:
        refresh_token = RefreshToken(refresh_token_str)
        new_access_token = str(refresh_token.access_token)
        return {
            'access': new_access_token,
            # Optionally return the same refresh token or issue a new one:
            'refresh': str(refresh_token),
        }
    except TokenError as e:
        return {'error': str(e)}


@api_view(['POST'])
def get_new_token(request):
    data = request.data
    refresh = str(data['refresh'])
    data = refresh_access_token(refresh)
    return Response(data=data, status=HTTP_400_BAD_REQUEST)