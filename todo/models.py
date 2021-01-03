from django.db import models
from django.utils import timezone
# Create your models here.
from django.urls import reverse

class Todo(models.Model):
    todo_title = models.CharField(max_length=50, blank=True)
    published_date = models.DateTimeField(default=timezone.now)

    # def get_absolute_url(self):
    #     return reverse("todo:todo_list")

    def __str__(self):
        return self.todo_title

class TodoPosts(models.Model):
    todo = models.ForeignKey(
        Todo, 
        on_delete=models.CASCADE)
    todo_post = models.CharField(max_length=150, blank=False)
    complete = models.BooleanField(default=False, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.todo_post

    class Meta:
        ordering = ["-published_date"]