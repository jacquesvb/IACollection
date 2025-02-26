from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, MediaSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Medium

class MediaListCreate(generics.ListCreateAPIView):
  serializer_class = MediaSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    return Medium.objects.filter(user=user)
  
  def perform_create(self, serializer):
    if serializer.is_valid():
      serializer.save(user=self.request.user)
    else:
      print(serializer.errors)


class MediaDelete(generics.DestroyAPIView):
  serializer_class = MediaSerializer
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    return Medium.objects.filter(user=user)


class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]
