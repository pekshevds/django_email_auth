from django.contrib.auth import login, logout
from django.shortcuts import (
    render,
    redirect
)
from django.http import (
    HttpResponse,
    HttpRequest
)
from django.views import View
from auth_app.forms import (
    SendEmailForm,
    LoginForm
)
from auth_app.services import (
    send_message,
    user_by_email,
    authenticate,
    deactivate_token
)


# {server}/auth/handle/?email=admin@mail.ru&token=2134213413413412341
class AuthHandlerView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.GET)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            token = form.cleaned_data.get("token")
            user = authenticate(email, token)
            if user:
                login(request, user)
                deactivate_token(token)
                return redirect("index:index")
        return redirect("auth:login")


class LoginView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form = SendEmailForm()
        return render(request, "auth_app/index.html", {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = SendEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = user_by_email(email=email)
            if user:
                send_message(
                    request,
                    reciver=user.email,
                    token=user.new_token())
                return redirect("index:index")
        return redirect("auth:login")


class logoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        logout(request)
        return redirect("index:index")
