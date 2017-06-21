from django.core.management import BaseCommand
from openpyxl import *
from todoapp.models import *
from django.contrib.auth.models import *

class Command(BaseCommand):
    help="""This Populates A Sample Data of 5 To Do Lists with 5 entries each"""

    def handle(self, *args, **options):
        one = User.objects.get(id=1)
        two = User.objects.get(id=2)
        ToDoList(name="List1",creation_date="2017-02-10",user=one).save()
        ToDoList(name="List2", creation_date="2017-09-03",user=two).save()
        ToDoList(name="List3", creation_date="2017-06-02",user=one).save()
        ToDoList(name="List4", creation_date="2017-07-11",user=one).save()
        ToDoList(name="List5", creation_date="2017-04-12",user=two).save()
        #List1:
        c=ToDoList.objects.get(name="List1")
        ToDoItem(description="Item1",completed=False,due_by="2019-03-01",parent=c).save()
        ToDoItem(description="Item2", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item3", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item4", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item5", completed=False, due_by="2019-03-01", parent=c).save()
        # List2:
        c = ToDoList.objects.get(name="List2")
        ToDoItem(description="Item6", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item7", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item8", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item9", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item10", completed=False, due_by="2019-03-01", parent=c).save()
        # List3:
        c = ToDoList.objects.get(name="List3")
        ToDoItem(description="Item11", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item12", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item13", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item14", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item15", completed=False, due_by="2019-03-01", parent=c).save()
        # List4:
        c = ToDoList.objects.get(name="List4")
        ToDoItem(description="Item16", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item17", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item18", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item19", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item20", completed=False, due_by="2019-03-01", parent=c).save()
        # List5:
        c = ToDoList.objects.get(name="List5")
        ToDoItem(description="Item21", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item22", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item23", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item24", completed=False, due_by="2019-03-01", parent=c).save()
        ToDoItem(description="Item25", completed=False, due_by="2019-03-01", parent=c).save()

        print "Sample Data Saved"

        pass

    pass
