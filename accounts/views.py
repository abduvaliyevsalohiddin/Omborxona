from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        pass
