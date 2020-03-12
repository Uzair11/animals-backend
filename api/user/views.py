from django.shortcuts import render
from libs.authentication import UserAuthentication
from libs.permission import UserAccessPermission, CustomerPermission
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class UserView(RetrieveUpdateAPIView):
    authentication_classes = (UserAuthentication,)
    permission_classes = (CustomerPermission, UserAccessPermission,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
