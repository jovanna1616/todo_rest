from rest_framework import serializers
from todos.models import Todo
# from django.contrib.auth.models import User
from users.models import CustomUser
# from rest_framework.validators import UniqueValidator
# from rest_framework.validators import UniqueTogetherValidator
from todos.validators import validate_todo_title

class TodoSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=10)   # works
    title = serializers.CharField(max_length=10, validators=[validate_todo_title])   # works

    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Todo
        
        
        # not working
        # title = serializers.CharField(validators=[UniqueValidator(queryset=Todo.objects.all(), message="Test validation message for title")],),
        
        # working
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Todo.objects.all(),
        #         fields=['title', 'content'],
        #         message="Custom validation message"
        #     )
        # ]
        fields = ['id', 'title', 'content', 'created_at', 'created_by']
        

