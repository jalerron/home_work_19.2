from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
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
        new_user.user_token = token_generator.make_token(new_user)
        form.save()
        register_confirm_ = register_confirm(self.request, user=new_user)
        if not new_user.is_active:
            send_mail(
                subject="Подтверждение почты",
                message=register_confirm_['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verify_email')


class EmailVerifyView(View):
    success_url = 'users/verified_email.html'

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user

    def get(self, request, uidb64, user_token):

        user = self.get_user(uidb64)

        if user is not None and user.user_token == user_token:
            user.is_active = True
            user.is_staff = True
            user.save()

            return render(request, 'users/verified_email.html')
        else:
            return render(request, 'users/verify_email.html') #Доделать шаблон неверного подтверждения


def verify_view(request):
    return render(request, 'users/verify_email.html')
