from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model

User=get_user_model()
# generate token function
def get_tokens_for_user(user):
    refresh= RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username=request.data.get("username")
    password=request.data.get("password")
    email=request.data.get("email")

    if User.objects.filter(username=username).exists():
        return Response({'err':"Username is already exists"})
    
    try:
        User.objects.create_user(
            username= username,
            email=email,
            password=password
        )
        return Response({"message":"User registered Successfully"},status= status.HTTP_200_OK)
    except Exception as e:
        return Response({'err':"Failed to register", "error":str(e)},status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username=request.data.get('username')
    password=request.data.get('password')

    if not username:
        return Response({'message':"Username is required"}, status= status.HTTP_400_BAD_REQUEST)
    elif not User.objects.filter(username=username).exists():
        return Response({'message':'Username doesnot exist'}, status= status.HTTP_400_BAD_REQUEST)

    if not password:
        return Response({'message':"Password is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    user=authenticate(username=username, password=password)
    if user is not None:
        tokens= get_tokens_for_user(user)
        return Response({
             "message":'Login user Successfully',
               'token':tokens
                 },status= status.HTTP_200_OK)
    else:
        return Response({'error':"Incorrect Password"},status= status.HTTP_400_BAD_REQUEST)

    



    










