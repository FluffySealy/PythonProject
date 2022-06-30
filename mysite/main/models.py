from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    #Add a foreign key for the user, every ToDoList will be related to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    #ToDoList name char field
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    #Adds a foreign key to the item, therefore every item will be related to a ToDoList
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    #text of item and boolean value fields.
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text