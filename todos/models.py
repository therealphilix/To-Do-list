from django.db import models
from django.conf import settings

# Create your models here.
class ToDoUser(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300, null=True, blank=True)
    completed = models.BooleanField(null=True)
    due_date = models.DateField(null=True)
    priority = models.BooleanField(null=True)
    todouser = models.ForeignKey(ToDoUser, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self) -> str:
        return self.title