from django.contrib import admin
from .models import ToDoList, Item
# Registered models.
admin.site.register(ToDoList)
admin.site.register(Item)