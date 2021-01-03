from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from todo.models import Todo, TodoPosts
from todo.forms import TodoForm, TodoPostForm
from django.urls import reverse



# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "todo/home_page.html"

class TodoListView(ListView):
    model = Todo
    template_name = "todo/todo_list_page.html"

    def get_queryset(self):
        return Todo.objects.order_by("-published_date")

class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/todo_create.html"
    form_class = TodoForm

    def form_valid(self, form):
        new_todo = form.save()
        return redirect("todo:todo_detail", pk=new_todo.pk)

class TodoPostUpdateView(UpdateView):
    model = TodoPosts
    form_class = TodoPostForm
    # redirect_field_name = 'todo/post_detail.html'

    def form_valid(self, form):
        new_todo_post = form.save()
        todo = new_todo_post.todo
        return redirect("todo:todo_detail", pk=todo.pk)

class TodoDetailView(FormMixin, DetailView):
    model = Todo
    template_name = "todo/todo_detail_page.html"
    form_class = TodoPostForm

def addTodoPost(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == "POST":
        form = TodoPostForm(request.POST)

        if form.is_valid():
            print("jo men det är giltigt")
            todo_post = form.save(commit=False)
            todo_post.todo = todo
            todo_post.save()
            return redirect('todo:todo_detail', pk=todo.pk)
        else:
            print("nej tyvärr det var ogiltigt")
        # print(request.method)
        # print("Här är posten")
        # print(request.POST["todo_post"])
    else:
        print("NOPE")
    # selected_todo = todo.todopost_set()

def removeTodoPost(request, todo_post_id):
    todo_post = get_object_or_404(TodoPosts, pk=todo_post_id)
    todo = todo_post.todo
    todo_post.delete()

    return redirect('todo:todo_detail', pk=todo.pk)

def completeTodoPost(request, todo_post_id):
    todo_post = get_object_or_404(TodoPosts, pk=todo_post_id)
    todo_post.complete = not todo_post.complete 
    todo = todo_post.todo
    todo_post.save()
    return redirect('todo:todo_detail', pk=todo.pk)
