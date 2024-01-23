from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm


def home(request):
    qs = Task.objects.get(id=2)
    context = {'task': qs}
    return render(request, 'index.html', context=context)


def register(request):
    return render(request, 'register.html')


def my_login(request):
    return render(request, 'my-login.html')


def createTask(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'task-form.html', context=context)

# def createTask(request):
#     form = TaskForm()
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view-tasks')
#     context = {'form': form}
#     return render(request, 'create-task.html', context=context)
#
#
# def viewTasks(request):
#     tasks = Task.objects.all()
#     context = {'tasks': tasks}
#     return render(request, 'view-tasks.html', context=context)
