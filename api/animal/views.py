from django.shortcuts import render
from libs.authentication import UserAuthentication
from .serializers import AnimalSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Animal
from rest_framework import status
import copy

# Create your views here.
class AnimalListView(ListCreateAPIView):
    authentication_classes = (UserAuthentication,)
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Animal.objects.filter(user__id=user_id).order_by('-created')
        return queryset

    def post(self, request, *args, **kwargs):
        request_data = copy.copy(request.data)
        user = self.request.user
        serializer = AnimalSerializer(data=request_data, context={"user": user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(str(serializer.error_messages), status=status.HTTP_400_BAD_REQUEST)


class AnimalView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (UserAuthentication,)
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def get_serializer_context(self):
        request_data = copy.copy(self.request.user)
        return {'user': request_data.id}

    def get_queryset(self):
        base_qs = super(AnimalView, self).get_queryset()
        return base_qs.filter(user=self.request.user)
