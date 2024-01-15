import uuid
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

from django.urls import reverse_lazy

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
        return reverse_lazy('catalog:product_list')

    # def form_valid(self, form):
    #     request = super().form_valid(form)
    #     user = form.save(commit=False)
    #     user.is_active = False
    #     user.save()
    #
    #     # Функционал для отправки письма и генерации токена
    #     token = default_token_generator.make_token(user)
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     activation_url = reverse_lazy('confirm_email', kwargs={'uidb64': uid, 'token': token})
    #     current_site = get_current_site(request)
    #     send_mail(
    #         'Подтвердите свой электронный адрес',
    #         f'Пожалуйста, перейдите по следующей ссылке, чтобы подтвердить свой адрес электронной почты: http://{current_site}{activation_url}',
    #         'service.notehunter@gmail.com',
    #         [user.email],
    #         fail_silently=False,
    #     )
    #     return redirect('catalog:index')
