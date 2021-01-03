from django.urls import path
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("todos/", views.TodoListView.as_view(), name="todo_list"),
    path("todos/new/", views.TodoCreateView.as_view(), name="new"),
    path("todos/<int:pk>/", views.TodoDetailView.as_view(), name="todo_detail"),
    path("todos/<int:todo_id>/add/", views.addTodoPost, name="add_todo_post"),
    path("todos/<int:todo_post_id>/remove/", views.removeTodoPost, name="remove_todo_post"),
    path("todos/<int:todo_post_id>/complete/", views.completeTodoPost, name="complete_todo_post"),
    path("todos/<int:pk>/edit/", views.TodoPostUpdateView.as_view(), name="edit_todo_post"),
]