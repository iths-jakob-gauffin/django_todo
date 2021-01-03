from django.contrib import admin
from django.urls import path, include
from accounts import views
# from todo import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup")
]