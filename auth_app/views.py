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
from auth_app.services import send_message


# {server}/auth/handle/?email=admin@mail.ru&token=2134213413413412341
class AuthHandlerView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = LoginForm(request.GET)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            token = form.cleaned_data.get("token")
            # print(f"email - {email}, token - {token}")
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
            send_message(request, reciver=email)
            return redirect("index:index")
        return redirect("auth:login")


class logoutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return redirect("index:index")
