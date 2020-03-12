from rest_framework import serializers
from api.user.models import User
from .models import Animal
from ..user.serializers import UserSerializer
import copy

class AnimalSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects)

    class Meta:
        model = Animal
        fields = ('id', 'name', 'dob', 'user', 'type')

    def create(self, validated_data):
        instance = super(AnimalSerializer, self).create(validated_data)
        return instance

    def to_internal_value(self, data):
        new_data = copy.copy(data)
        if "user" not in data:
            new_data["user"] = User(id=self.context["user"])
        return new_data

    def to_representation(self, instance):
        data = super(AnimalSerializer, self).to_representation(instance)
        if instance.user:
            data['user'] = UserSerializer(instance.user).data
        return data
