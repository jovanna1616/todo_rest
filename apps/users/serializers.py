from rest_framework import serializers
# from django.contrib.auth.models import User
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    todos = serializers.HyperlinkedRelatedField(many=True, view_name='todo-detail', read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'todos']

