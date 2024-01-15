from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import View

from django.views.generic import CreateView


from users.forms import UserRegisterForm
from users.models import User
from users.utils import register_confirm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form, *args, **kwargs):

        new_user = form.save()
        register_confirm_ = register_confirm(self.request, user=new_user)
        if not new_user.email_verify:
            send_mail(
                subject="Подтверждение почты",
                message=register_confirm_['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verify_email')


def verify_view(request):
    return render(request, 'users/verify_email.html')
