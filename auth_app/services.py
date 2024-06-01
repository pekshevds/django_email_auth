from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_message(
        request: HttpRequest,
        reciver: str, token: str = "") -> None:
    host = request.build_absolute_uri().\
        replace(request.get_full_path(), "")
    context = {
        "host": host,
        "email": reciver,
        "token": token,
    }
    html_message = render_to_string(
        template_name="auth_app/message.html",
        context=context
    )
    send_mail(
        subject="Для входа на сайт передите по ссылке",
        message=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[reciver]
        )
