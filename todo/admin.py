from django.contrib import admin
from django.urls import path, include   
from todo.models import TodoItem

admin.site.register(TodoItem)