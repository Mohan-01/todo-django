from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.text import slugify
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'dead_line', 'completed']
        
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "title", "class": "form-control"}))
    dead_line = forms.CharField(label="", widget=forms.DateTimeInput(attrs={"placeholder": "dead_line", "class": "form-control", "type": "datetime-local"}))
    completed = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "checkbox", "value": False}), required=False)
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class": "form-control"}))
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UpdateUser(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', ]