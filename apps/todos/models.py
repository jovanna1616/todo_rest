from django.db import models
from users.models import CustomUser


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('users.CustomUser', related_name='todos', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
