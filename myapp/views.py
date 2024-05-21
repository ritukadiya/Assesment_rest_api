from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskList(generics.ListCreateAPIView):
	queryset=Task.objects.all()
	serializer_class=TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Task
	serializer_class=TaskSerializer