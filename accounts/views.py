from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        user = authenticate(
            username=request.POST.get("login"),
            password=request.POST.get("password")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/asosiy/bolimlar/")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")
