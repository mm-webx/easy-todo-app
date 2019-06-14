from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('is_completed')
    serializer_class = TodoSerializer