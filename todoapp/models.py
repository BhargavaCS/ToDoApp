# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=128)
    creation_date = models.DateField(null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.name


class ToDoItem(models.Model):
    description = models.CharField(max_length=512)
    completed = models.BooleanField(default=False)
    due_by = models.DateField(null=False)
    parent = models.ForeignKey(ToDoList)

    def __unicode__(self):
        return str(self.due_by)




