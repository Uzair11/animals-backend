from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..user.serializers import UserSerializer
from libs.jwt_helper import JWTHelper

User = get_user_model()


class UserTokenSerializer(UserSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, user_request):
        user = JWTHelper.encode_token(user_request)
        return user
