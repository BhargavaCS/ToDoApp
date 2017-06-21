from rest_framework import serializers
from todoapp.models import *


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id','name', 'creation_date', 'user')


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id','description', 'completed', 'due_by', 'parent')


