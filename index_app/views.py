from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpRequest
)
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index_app/index.html", {})
