from django.core.exceptions import ValidationError

def validate_todo_title(value):
    if not "Buy" in value:
        raise ValidationError("Title must start with Buy")
    else:
        return value
