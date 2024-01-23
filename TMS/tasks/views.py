from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse


# from .forms import TaskForm
#
#
def home(request):
    return render(request, 'index.html')


def register(request):
    return HttpResponse('This is registration page!')

    # return render(request, 'register.html')


def my_login(request):
    return HttpResponse('This is the login page!')
    # return render(request, 'my-login.html')
#
#
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
