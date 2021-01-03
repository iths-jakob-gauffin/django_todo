from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import UserCreateForm 
# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

