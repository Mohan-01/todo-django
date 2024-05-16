from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from . import forms
from . import models

# Create your views here.
def home(req):
    user_id = req.session.get('user_id', None)
    
    if user_id == None:
        return render(req, 'todo/index.html', {'message': 'Login to see your tasks', 'user': None})
    user = User.objects.get(id=user_id)
    print(user)
    todos = models.Task.objects.filter(user_id=user.id)
    return render(req, 'todo/index.html', {'todos': todos, "user": user})

@login_required
def addTask(req):
    print(req.session.items())
    if req.method == 'POST':
        form = forms.TaskForm(req.POST)
        if(form.is_valid()):
            title = form.cleaned_data['title']
            dead_line = form.cleaned_data['dead_line']
            user = User.objects.get(id=req.session['user_id'])
            
            task = models.Task(user=user, title=title, dead_line=dead_line, slug=slugify(title))
            task.save()
            
            return redirect('ListTasks')
    form = forms.TaskForm()
    return render(req, 'todo/addTask.html', {'form': form, 'submit': 'Add Task'})

@login_required
def editTask(req, **kwargs):
    task = models.Task.objects.get(slug=kwargs['slug'])
    if req.method == 'POST':
        form = forms.TaskForm(req.POST, instance=task)
        if(form.is_valid()):
            form.save()
            return redirect('ListTasks')
    form = forms.TaskForm(instance=task)
    return render(req, 'todo/addTask.html', {'form': form, 'submit': 'Edit Task'})

@login_required
def deleteTask(req, **kwargs):
    task = models.Task.objects.get(slug=kwargs['slug'])
    task.delete()
    return redirect('ListTasks')


# Sign up
@csrf_protect
def user_signup(req):
    if req.method == 'POST':
        form = forms.RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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
                req.session['user_id'] = user.id
                return redirect('home')
            else:
                print('Wrong username or password')
        else:
            print('form is not valid')
    form = forms.LoginForm()
    return render(req, 'todo/login.html', {'form': form})

@login_required
def user_logout(req):
    logout(req)
    return redirect('home')

@login_required
def user_profile(req):
    user = User.objects.get(id=req.session.get('user_id'))
    return render(req, 'todo/profile.html', {'user': user})