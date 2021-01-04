from django.db import models
from django.utils import timezone
# Create your models here.
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# User = get_user_model()

class Todo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE, blank=True, null=True)
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