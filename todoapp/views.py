# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from rest_framework import generics
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import *
from todoapp.Serializers import *
from django.http import *

# Create your views here.


def ShowLists(request):
    all_lists = ToDoList.objects.all().filter(user__username=request.user)
    print all_lists,request.user
    context = {'all_lists': all_lists}
    return render(request, 'all_lists.html', context)


def ShowItems(request, id):
    items = ToDoItem.objects.all().filter(parent__id=id)
    context = {'items':items}
    return render(request,'details.html',context)


class CreateList(LoginRequiredMixin, CreateView):
    model = ToDoList
    login_url = 'login'
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    fields = ['name', 'creation_date', 'user']
    success_url = reverse_lazy('lists')

    def post(self, request, *args, **kwargs):
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        a = ToDoList()
        a.name = self.request.POST['name']
        a.creation_date = date
        a.user = User.objects.get(username=request.user)
        a.save()
        print a,"sbr"
        return HttpResponseRedirect('/todoapp/lists')
        pass


class UpdateList(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = ToDoList
    permission_required = 'todoapp.change_todolist'
    raise_exception=False
    login_url = 'login'
    fields = ['name']
    success_url = reverse_lazy('lists')
    permission_denied_message = "No Permissions To View This Content"

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied(self.permission_denied_message)
        return super(UpdateList, self).handle_no_permission()
    pass


class DeleteList(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ToDoList
    login_url = 'login'
    permission_required = 'todoapp.delete_todolist'
    raise_exception = False
    fields = ['name']
    success_url = reverse_lazy('lists')
    permission_denied_message = "No Permissions To View This Content"

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied(self.permission_denied_message)
        return super(DeleteList, self).handle_no_permission()

    pass
    pass


#######################-----Rest-APIs-----------######################

class rest_lists(generics.ListCreateAPIView):
    def get_queryset(self):
        return ToDoList.objects.all().filter(user__username=self.request.user)

    serializer_class = ToDoListSerializer


class rest_lists_id(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return ToDoList.objects.all().filter(user__username=self.request.user).get(pk=self.kwargs['pk'])

    serializer_class = ToDoListSerializer


class rest_items(generics.ListCreateAPIView):
    def get_queryset(self):
        return ToDoItem.objects.all().filter(parent__user__username=self.request.user)

    serializer_class = ToDoItemSerializer


class rest_items_id(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self):
        return ToDoItem.objects.all().filter(parent__user__username=self.request.user).get(pk=self.kwargs['pk'])

    serializer_class = ToDoItemSerializer


class rest_list_id_items_id(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoItemSerializer

    def get_object(self, queryset=None):
        try:
            return ToDoItem.objects.filter(parent__user___username=self.request.uer).filter(parent__id=self.kwargs['list_id']).get(id=self.kwargs['item_id'])
        except:
            return Http404

    def put(self, request, *args, **kwargs):
        request.data['parent'] = self.kwargs['list_id']
        return self.update(request, *args, **kwargs)


class rest_list_id_items(generics.ListCreateAPIView):
    serializer_class = ToDoItemSerializer

    def get_queryset(self, queryset=None):
        try:
            return ToDoItem.objects.filter(parent__user__username=self.request.user).filter(parent__id=self.kwargs['list_id'])
        except:
            return Http404

    def post(self, request, *args, **kwargs):
        request.data['parent'] = self.kwargs['list_id']
        return self.create(request, *args, **kwargs)





