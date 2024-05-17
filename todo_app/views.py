from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from . import forms
from . import models

# Create your views here.
def home(req):
    if req.user.is_authenticated:
        todos = models.Task.objects.filter(user_id=req.user.id)
        return render(req, 'todo/index.html', {'todos': todos, "user": req.user})
    messages.success(req, 'Login to see your tasks')
    return render(req, 'todo/index.html')

@login_required
def addTask(req):
    if req.method == 'POST':
        form = forms.TaskForm(req.POST)
        if(form.is_valid()):
            title = form.cleaned_data['title']
            dead_line = form.cleaned_data['dead_line']
            user = User.objects.get(id=req.user.id)
            
            task = models.Task(user=user, title=title, dead_line=dead_line, slug=slugify(title))
            task.save()
            messages.success(req, 'Task added successfully')
            return redirect('ListTasks')
        else:
            messages.error(req, 'Task not added')
    form = forms.TaskForm()
    return render(req, 'todo/addTask.html', {'form': form, 'submit': 'Add Task'})

@login_required
def editTask(req, **kwargs):
    task = models.Task.objects.get(slug=kwargs['slug'])
    if req.method == 'POST':
        form = forms.TaskForm(req.POST, instance=task)
        if(form.is_valid()):
            form.save()
            messages.success(req, 'Task updated successfully')
            return redirect('ListTasks')
    form = forms.TaskForm(instance=task)
    return render(req, 'todo/addTask.html', {'form': form, 'submit': 'Edit Task'})

@login_required
def deleteTask(req, **kwargs):
    task = models.Task.objects.get(slug=kwargs['slug'])
    task.delete()
    messages.success(req, 'Task deleted successfully')
    return redirect('ListTasks')


# Sign up
def user_signup(req):
    if req.method == 'POST':
        form = forms.RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, ('Registed successfully.. You can now login'))
            return redirect('login')
    form = forms.RegisterForm()
    return render(req, 'todo/signup.html', {'form': form})

# @csrf_protect
def user_login(req):
    if req.method == 'POST':
        form = forms.LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(req, username=username, password=password)
            if user:
                login(req, user)
                messages.success(req, ('Logged in successfully'))
                return redirect('home')
            else:
                messages.error(req, 'Wrong username or password')
        else:
            print('form is not valid')
    form = forms.LoginForm()
    return render(req, 'todo/login.html', {'form': form})

@login_required
def user_logout(req):
    logout(req)
    messages.success(req, ('Logged out successfully'))
    return redirect('home')

@login_required
def user_profile(req):
    user = User.objects.get(id=req.user.id)
    return render(req, 'todo/profile.html', {'user': user})

@login_required
def update_user(req):
    user = User.objects.get(id=req.user.id)
    form = forms.UpdateUser(req.POST or None, instance=user)
    if req.method == 'POST':
        if form.is_valid():
            form.save()
            login(req, user)
            messages.success(req, 'Updated successfully')
            return redirect('home')
    return render(req, 'todo/updateUser.html', {'form': form})