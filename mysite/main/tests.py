from django.test import TestCase
from .models import ToDoList, Item

#A test to test the creation of to do lists
class ToDoListTestCase(TestCase):
    def setUp(todolist):
        todolist.objects.create(name="TST-1", sound="roar")
        todolist.objects.create(name="TST-2", sound="meow")
        
#This then sees if the tasks above have ran and checks their status        
def test_todolists_exist(todolist):
        """Tests that return a value are ToDoLists that have been created successfully"""
        test1 = todolist.objects.get(name="TST-1")
        test2 = todolist.objects.get(name="TST-2")
        todolist.assertEqual(test1.speak(), 'TST-1 was successful')
        todolist.assertEqual(test2.speak(), 'TST-2 was successful')