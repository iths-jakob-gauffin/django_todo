from django import forms
from todo import models

class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ("todo_title",)

class TodoPostForm(forms.ModelForm):
    class Meta:
        model = models.TodoPosts
        fields = ("todo_post",)