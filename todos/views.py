from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TaskSerializer, UpdateTaskSerializer, ToDoUserSerializer, CreateTaskSerializer
from .models import Task, ToDoUser

# Create your views here.
class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateTaskSerializer(
            data=request.data,
            context={'user_id': self.request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def get_queryset(self):
        return Task.objects.filter(todouser__user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UpdateTaskSerializer
        return TaskSerializer
    
class ToDoUserViewSet(ModelViewSet):
    queryset = ToDoUser.objects.all()
    serializer_class = ToDoUserSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (todouser,created) = ToDoUser.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = ToDoUserSerializer(todouser)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ToDoUserSerializer(todouser, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)