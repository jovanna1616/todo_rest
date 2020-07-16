from django.shortcuts import render
from todos.models import Todo
from todos.serializers import TodoSerializer
from django.contrib.auth.models import User
from users.models import CustomUser
from users.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from todos.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

