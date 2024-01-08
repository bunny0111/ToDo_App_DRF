# from rest_framework import generics  # This is views.py

from rest_framework import viewsets 
from ToDo import models
from .serializers import TodoSerializer

'''
class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
'''

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

'''
As you build more and more APIs you'll start to see the same patterns over and over again. Most API endpoints are some combination of common CRUD (Create-Read-Update-Delete) functionality. Instead of writing these views one-by-one in our views.py file as well as providing individual routes for each in our urls.py file we can instead use a ViewSet which abstracts away much of this work.

The viewsets class does all the magic here, specifically the method ModelViewSet which automatically provides list as well as create, retrieve, update, and destroy actions for us.
'''