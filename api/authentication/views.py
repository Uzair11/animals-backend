from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from libs.authentication import UserAuthentication
from .serializers import UserTokenSerializer
from rest_framework import status
from django.contrib.auth import authenticate, logout
from libs.custom_exceptions import (
    InvalidInputDataException,
    InvalidCredentialsException,
    UserExistsException,
    UserNotAllowedException,
    UserDoesNotExistsException,
    VerificationException)

# Create your views here.
User = get_user_model()


class RegistrationView(APIView):
    """
    View for registering a new user to your system.
    **Example requests**:
        POST /auth/register/
    """

    def post(self, request):
        if not User.is_exists(request.data['email']):
            serializer = UserTokenSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                RegistrationView.update_user_status(request.data['email'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            raise InvalidInputDataException(str(serializer.errors))
        raise UserExistsException()

    @staticmethod
    def update_user_status(user_email):
        user = User.objects.get(email=user_email)
        user.active = True
        user.save()


class LoginView(APIView):
    """
    View for login a user to your system.
    **Example requests**:
        POST /auth/login/
    """

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(email=email, password=password)
        if user:
            if user.active:
                serializer = UserTokenSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                raise UserNotAllowedException()
        else:
            if not User.is_exists(request.data['email']):
                raise UserDoesNotExistsException()
            else:
                raise InvalidCredentialsException()


class LogoutView(APIView):
    """
    View for logout a user to your system.
    **Example requests**:
        POST /auth/logout/
    """

    authentication_classes = (UserAuthentication,)

    def post(self, request):
        # any operation want to perform at logout
        logout(request)
        return Response({}, status=status.HTTP_200_OK)
