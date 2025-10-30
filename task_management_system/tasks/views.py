from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Comment
from .forms import TaskForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def task_list(request):
    if request.user.role == 'admin':
        tasks = Task.objects.all()
    elif request.user.role == 'teacher':
        tasks = Task.objects.filter(assigned_to=request.user) | Task.objects.filter(created_by=request.user)
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'Completed'
    task.save()
    return redirect('task_list')

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user == task.created_by or request.user.role == 'admin':
        task.delete()
    return redirect('task_list')

@login_required
@role_required(['admin', 'teacher']) # type: ignore
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required
@role_required(['admin', 'teacher']) # type: ignore
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
@role_required(['admin']) # type: ignore
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

@login_required
def task_list(request):
    if request.user.role == 'admin':
        tasks = Task.objects.all()
    elif request.user.role == 'teacher':
        tasks = Task.objects.filter(assigned_to=request.user) | Task.objects.filter(created_by=request.user)
    else:  # student
        tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})