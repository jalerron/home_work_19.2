from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as token_generator


def register_confirm(request, user):
    current_site = get_current_site(request)
    context = {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token_generator.make_token(user),
    }

    message = f'http://{current_site}/{context["uid"]}/{context["token"]}'
    data = {
        'current_site': current_site,
        'context': context,
        'message': message,
    }
    return data

    # message = render_to_string(
    #     'users/verify_email.html',
    #     context=context
    # )
