from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

from users.models import User


class RegisterView(CreateView):
    model = User
    from_class = UserCreationForm
    template_name = 'users/register.html'
    fields = ('__all__')
