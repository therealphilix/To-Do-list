from rest_framework import serializers
from .models import Task, ToDoUser

class ToDoUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = ToDoUser
        fields = ['id', 'user_id', 'phone', 'birth_date']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'due_date', 'priority',]

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed']

class CreateTaskSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_blank=True)
    completed = serializers.BooleanField(default=False)
    due_date = serializers.DateField(required=True)
    priority = serializers.BooleanField(required=False, allow_null=True)

    def create(self, validated_data):
        todouser = ToDoUser.objects.get(user_id=self.context['user_id'])
        return Task.objects.create(todouser=todouser, **validated_data)
