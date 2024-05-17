from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# from django.core import validators

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=80)
#     password = models.CharField(validators=[
#         validators.MinLengthValidator(8, 'Password must be at least 8 characters')
#     ], max_length=32)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, unique=True, primary_key=True)
    dead_line = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', null=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)
        
    def delete_everything(self):
        Task.objects.all().delete()
    
    