from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, unique=True, primary_key=True)
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
    
    