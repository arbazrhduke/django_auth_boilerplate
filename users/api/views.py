from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import LoginSerializer


class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(email=serializer.data.get('email'),
                                password=serializer.data.get('password'))
            if user is not None:
                return Response({"message": "Login Successful", "data": {
                    "token": Token.objects.get_or_create(user=user)[0].key}},
                                status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "Email or Password Incorrect", "data":
                        serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST)
