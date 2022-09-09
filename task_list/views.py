from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_list.forms import TaskForm
from task_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list:task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list:task-list')


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.status is True:
        task.status = False
        task.save()
    else:
        task.status = True
        task.save()
    return HttpResponseRedirect(reverse_lazy('task_list:task-list'))


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('task_list:task-list')


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('task_list:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy('task_list:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('task_list:tag-list')
