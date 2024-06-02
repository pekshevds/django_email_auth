from typing import Union
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from auth_app.models import User, Token


def authenticate(email: str, token: str) -> Union[User, None]:
    user = user_by_email(email)
    if user:
        _token = token_by_id(id=token, user=user)
        if _token and _token.is_active:
            return user
    return None


def token_by_id(id: str, user: User) -> Union[Token, None]:
    return Token.objects.filter(id=id, user=user).first()


def deactivate_token(token: str) -> bool:
    _token = Token.objects.filter(id=token).first()
    _token.is_active = False
    _token.save()
    return True


def user_by_email(email: str) -> Union[User, None]:
    return User.objects.filter(email=email).first()


def send_message(
        request: HttpRequest,
        reciver: str, token: str) -> None:
    host = request.build_absolute_uri().replace(request.get_full_path(), "")
    link = f"{host}/auth/handle/?email={reciver}&token={token}"
    context = {
        "link": link
    }
    html_message = render_to_string(
        template_name="auth_app/message.html",
        context=context
    )
    send_mail(
        subject="Для входа на сайт передите по ссылке",
        message=f"Для входа на сайт передите по ссылке {link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        fail_silently=True,
        recipient_list=[reciver],
        html_message=html_message
        )
