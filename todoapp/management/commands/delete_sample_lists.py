from django.core.management import BaseCommand
from openpyxl import *
from todoapp.models import *

class Command(BaseCommand):
    help="Deleting The Sample Data"

    def handle(self,*args,**options):
        ToDoList.objects.all().delete()
        ToDoItem.objects.all().delete()
        print "Sample Data Cleared"
        pass
    pass
