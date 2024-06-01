import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.db import models
import config


class User(AbstractUser):
    password = models.CharField(
        _("password"),
        max_length=128,
        default=make_password(config.AUTH_USER_DEFAULT_PASSWORD)
    )
    email = models.EmailField(_("email address"),
                              unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Token(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        related_name="tokens",
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name="Активный токен",
        default=True
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.id}"

    class Meta:
        verbose_name = "Токен"
        verbose_name_plural = "Токены"
