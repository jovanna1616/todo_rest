from rest_framework import serializers
from todos.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    created_by = serializers.HyperlinkedRelatedField(view_name='todo-creator', read_only=True)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'content', 'created_at', 'created_by']

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'todos']



