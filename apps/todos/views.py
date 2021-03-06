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
class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def creator(self, request, *args, **kwargs):
        todo = self.get_object()
        return Response(todo.created_by.username.upper())

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

