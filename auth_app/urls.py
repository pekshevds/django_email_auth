from django.urls import path
from auth_app.views import (
    LoginView,
    logoutView,
    AuthHandlerView
)

app_name = "auth"

urlpatterns = [
    path("handle/", AuthHandlerView.as_view(), name="auth-handel"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logoutView.as_view(), name="logout"),
]
